import os
import sys
import glob
import numpy as np
import pandas as pd
import logging
import ast
from collections.abc import Iterable
from transformers import TapasTokenizer, TapasForQuestionAnswering
import torch

def setup_logging(log_file):
    """Configure logging for the script."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'  # Append to the log file
    )
    # Also log to console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def clean_cell(cell):
    """Clean individual cell data."""
    if isinstance(cell, (list, tuple, pd.Series, np.ndarray)):
        if all(pd.isnull(x) for x in cell):
            return ""
        else:
            return ", ".join(map(str, cell))
    elif isinstance(cell, (np.ndarray, pd.Series)) and pd.isnull(cell).all():
        return ""
    elif pd.isnull(cell):
        return ""
    else:
        return str(cell)

def get_numeric_prefix(filename):
    """
    Extract the numeric prefix from a filename.

    Args:
        filename (str): Filename (e.g., '050_ING.parquet')

    Returns:
        int: Numeric prefix as integer (e.g., 50)
    """
    try:
        prefix = filename.split('_')[0]
        return int(prefix)
    except (IndexError, ValueError):
        return None

def fix_columns_used(columns_used_raw):
    """
    Process the 'columns_used' field to ensure it is a list of strings.

    Args:
        columns_used_raw (str or list or np.ndarray): The raw 'columns_used' value.

    Returns:
        list: A clean list of column names.

    Raises:
        TypeError: If 'columns_used' is not a string, list, or numpy array.
        ValueError: If 'columns_used' cannot be converted to a list of strings.
    """
    if isinstance(columns_used_raw, str):
        # Remove null bytes and strip whitespace
        columns_used_clean = columns_used_raw.replace('\x00', '').strip()

        # Safely evaluate the string to a Python list
        try:
            columns_used = ast.literal_eval(columns_used_clean)
            if not isinstance(columns_used, list):
                raise ValueError(f"'columns_used' is not a list after evaluation: {columns_used}")
        except Exception as e:
            raise ValueError(f"Error evaluating 'columns_used' string: {e}")
    elif isinstance(columns_used_raw, (list, np.ndarray)):
        # Convert numpy array to list if necessary
        columns_used = list(columns_used_raw) if isinstance(columns_used_raw, np.ndarray) else columns_used_raw

        # Ensure all elements are strings
        if not all(isinstance(col, str) for col in columns_used):
            raise ValueError(f"Not all elements in 'columns_used' are strings: {columns_used}")

        # **Removed Splitting of Concatenated Column Names**
        # This prevents legitimate multi-word column names from being split incorrectly.
        # If you encounter truly concatenated column names without proper delimiters,
        # consider using a different approach or fixing the data source.

    else:
        raise TypeError(f"'columns_used' is neither a string, list, nor numpy array: {columns_used_raw}")

    # Final check to ensure all column names are strings
    if not all(isinstance(col, str) for col in columns_used):
        raise ValueError(f"'columns_used' contains non-string elements: {columns_used}")

    return columns_used

def process_questions_file(questions_file, tables_dir, output_dir, tokenizer, model, device):
    """
    Process a single questions file against its corresponding table.

    Args:
        questions_file (str): Path to the questions .parquet file.
        tables_dir (str): Directory containing table .parquet files.
        output_dir (str): Directory to save prediction output files.
        tokenizer: TapasTokenizer instance.
        model: TapasForQuestionAnswering instance.
        device: Torch device (CPU or GPU).
    """
    try:
        questions_filename = os.path.basename(questions_file)
        dataset_id = questions_filename.split('.')[0]  # e.g., '050_ING'
        table_file = os.path.join(tables_dir, f"{dataset_id}.parquet")

        logging.info(f"Processing questions file: {questions_filename}")
        logging.info(f"Corresponding table file: {table_file}")

        # Check if the corresponding table exists
        if not os.path.exists(table_file):
            error_msg = f"Table file {table_file} not found for questions file {questions_filename}."
            logging.error(error_msg)
            return

        # Load questions
        df_questions = pd.read_parquet(questions_file)
        logging.info(f"Loaded {len(df_questions)} questions from {questions_filename}.")

        # Load table
        df_table = pd.read_parquet(table_file)
        logging.info(f"Loaded table with {len(df_table)} rows from {dataset_id}.parquet.")

        # Iterate over each question
        predictions = []
        for index, row in df_questions.iterrows():
            logging.info(f"Processing question {index + 1}/{len(df_questions)} in {questions_filename}...")
            question_text = row['question']

            # Handle 'columns_used' field
            try:
                columns_used_raw = row['columns_used']
                columns_used = fix_columns_used(columns_used_raw)
                logging.info(f"'columns_used' resolved to: {columns_used}")
            except Exception as e:
                error_msg = f"Error evaluating 'columns_used' for question {index + 1}: {e}"
                logging.error(error_msg)
                predictions.append(error_msg)
                continue

            # Filter table columns
            try:
                df_filtered_table = df_table[columns_used]
                logging.info(f"Filtered table to columns: {columns_used}")
            except KeyError as e:
                error_msg = f"Error: {e} in dataset {dataset_id}."
                logging.error(error_msg)
                predictions.append(error_msg)
                continue

            # Clean the table
            df_filtered_table = df_filtered_table.applymap(clean_cell)
            logging.info("Cleaned the table data.")

            # Tokenize
            try:
                inputs = tokenizer(
                    table=df_filtered_table,
                    queries=[question_text],
                    padding='max_length',
                    return_tensors="pt"
                )
                logging.info("Tokenization successful.")
            except Exception as e:
                error_msg = f"Tokenization error for question {index + 1}: {e}"
                logging.error(error_msg)
                predictions.append(error_msg)
                continue

            # Move inputs to the appropriate device
            inputs = {k: v.to(device) for k, v in inputs.items()}

            # Inference
            try:
                outputs = model(**inputs)
                logging.info("Inference completed.")
            except Exception as e:
                error_msg = f"Inference error for question {index + 1}: {e}"
                logging.error(error_msg)
                predictions.append(error_msg)
                continue

            # Predictions
            try:
                # **Move Inputs to CPU Before Passing to convert_logits_to_predictions**
                inputs_cpu = {k: v.cpu() for k, v in inputs.items()}

                predicted_answer_coordinates, predicted_aggregation_indices = tokenizer.convert_logits_to_predictions(
                    inputs_cpu,
                    outputs.logits.detach().cpu(),
                    outputs.logits_aggregation.detach().cpu()
                )

                answers = []
                for coordinates in predicted_answer_coordinates:
                    if len(coordinates) == 1:
                        cell_value = df_filtered_table.iat[coordinates[0][0], coordinates[0][1]]
                        answers.append(str(cell_value))
                    else:
                        answer = [str(df_filtered_table.iat[coord[0], coord[1]]) for coord in coordinates]
                        answers.append(", ".join(answer))

                predicted_answer = " | ".join(answers)
                predictions.append(predicted_answer)
                logging.info(f"Predicted Answer: {predicted_answer}")
            except Exception as e:
                error_msg = f"Prediction extraction error for question {index + 1}: {e}"
                logging.error(error_msg)
                predictions.append(error_msg)
                continue

        # Write predictions to output file
        output_filename = os.path.splitext(questions_filename)[0] + "_predictions.txt"
        output_file = os.path.join(output_dir, output_filename)
        with open(output_file, "w") as f_out:
            for pred in predictions:
                f_out.write(f"{pred}\n")
        logging.info(f"Predictions written to {output_file}\n")

    except Exception as e:
        logging.error(f"An unexpected error occurred while processing {questions_file}: {e}", exc_info=True)

def main():
    try:
        # Setup logging
        log_file = "/data/shlok/prediction_dev_qa.log"
        setup_logging(log_file)
        logging.info("==============================================")
        logging.info("Starting TaPas Question Answering Script")
        logging.info("==============================================\n")

        # Define base directory
        base_dir = "/data/shlok/data"
        logging.info(f"Base directory set to: {base_dir}")

        # Define paths to questions and tables
        questions_dir = os.path.join(base_dir, "questions")
        tables_dir = os.path.join(base_dir, "lite")
        output_dir = os.path.join(base_dir, "predictions")

        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logging.info(f"Created output directory: {output_dir}")
        else:
            logging.info(f"Output directory: {output_dir}")

        # Define the range of files to process
        min_num = 50
        max_num = 65

        # Find all questions files within the specified range
        all_question_files = glob.glob(os.path.join(questions_dir, "*.parquet"))
        question_files = []
        for q_file in all_question_files:
            filename = os.path.basename(q_file)
            num_prefix = get_numeric_prefix(filename)
            if num_prefix is not None and min_num <= num_prefix <= max_num:
                question_files.append(q_file)

        if not question_files:
            logging.error(f"No .parquet files found in questions directory: {questions_dir} within range {min_num:03d} to {max_num:03d}.")
            sys.exit(1)

        logging.info(f"Found {len(question_files)} questions files to process (from {min_num:03d} to {max_num:03d}).\n")

        # Load the TaPas model and tokenizer
        logging.info("Loading the TaPas model and tokenizer...")
        tokenizer = TapasTokenizer.from_pretrained("google/tapas-large-finetuned-wtq")
        model = TapasForQuestionAnswering.from_pretrained("google/tapas-large-finetuned-wtq")
        logging.info("TaPas model and tokenizer loaded successfully.\n")

        # Move model to appropriate device (GPU if available)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
        logging.info(f"Using device: {device}\n")

        # Process each questions file
        for q_file in question_files:
            process_questions_file(q_file, tables_dir, output_dir, tokenizer, model, device)

        logging.info("==============================================")
        logging.info("TaPas Question Answering Script Completed Successfully")
        logging.info("==============================================")

    except Exception as e:
        logging.error(f"An unexpected error occurred in the main script: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()

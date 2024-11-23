import pandas as pd
import torch
from table_bert import TableBertModel, Table, Column
import sys
import json  # To format output in a shell-compatible way


def map_dtype(dtype):
    """
    Map pandas column data types to Table-BERT data types.

    Args:
        dtype: The pandas dtype of the column.

    Returns:
        A string representing the type ('real' or 'text') for Table-BERT.
    """
    if pd.api.types.is_numeric_dtype(dtype):
        return 'real'
    else:
        return 'text'


def prepare_table(df, model):
    """
    Prepares a table object from a pandas DataFrame for Table-BERT.

    Args:
        df: The pandas DataFrame to process.
        model: The Table-BERT model, used for tokenization.

    Returns:
        A Table object compatible with Table-BERT.
    """
    # Convert all categorical columns to string type
    for col in df.select_dtypes(include='category').columns:
        df[col] = df[col].astype(str)

    # Fill NaN values and convert the entire DataFrame to strings
    data = df.fillna('').astype(str).values.tolist()

    # Create the table header with sample values
    header = []
    for col in df.columns:
        dtype = map_dtype(df[col].dtype)
        # Use the first non-null value as a sample
        sample_value = df[col].dropna().iloc[0] if not df[col].dropna().empty else ""
        header.append(Column(name=col, type=dtype, sample_value=str(sample_value)))

    # Create and tokenize the Table object
    table = Table(
        id='001_Forbes',  # Identifier for the table
        header=header,
        data=data
    ).tokenize(model.tokenizer)

    return table


def main():
    # Check for CUDA availability
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load the Table-BERT model
    model_path = '/data/ankur/TaBERT/tabert_large_k3/model.bin'
    model = TableBertModel.from_pretrained(model_path).to(device)

    # Load the dataset from a parquet file
    parquet_file_path = '/data/shlok/data/full/001_Forbes.parquet'
    df = pd.read_parquet(parquet_file_path)

    # Prepare the table from the DataFrame
    table = prepare_table(df, model)

    # Define the context for the model
    context = "Name the richest person"

    # Encode the context and table using the Table-BERT model
    context_encoding, column_encoding, info_dict = model.encode(
        contexts=[model.tokenizer.tokenize(context)],
        tables=[table]
    )

    # Extract encoded data
    input_ids = info_dict['input_ids']
    segment_ids = info_dict['segment_ids']
    context_token_positions = info_dict['context_token_positions']
    column_token_position_to_column_ids = info_dict['column_token_position_to_column_ids']
    sequence_mask = info_dict['sequence_mask']
    context_token_mask = info_dict['context_token_mask']
    table_mask = info_dict['table_mask']

    # Pass the encoded inputs to the model
    outputs = model(
        input_ids=input_ids.to(device),
        segment_ids=segment_ids.to(device),
        context_token_positions=context_token_positions.to(device),
        column_token_position_to_column_ids=column_token_position_to_column_ids.to(device),
        sequence_mask=sequence_mask.to(device),
        context_token_mask=context_token_mask.to(device),
        table_mask=table_mask.to(device)
    )

    # Convert outputs to JSON-compatible format for shell use
    output_dict = {key: value.cpu().tolist() for key, value in outputs.items()}
    
    # Write the output to stdout as JSON
    sys.stdout.write(json.dumps(output_dict))
    sys.stdout.flush()


if __name__ == "__main__":
    # Execute the main function
    main()

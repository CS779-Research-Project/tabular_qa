import pickle
import json
from collections import Counter
import pandas as pd
from datasets import load_dataset

# Load the JSON data
with open('results/pyagent_phi35_sc_full.json', 'r') as f:
    data = json.load(f)
# with open('results/phi35_dp_lite.pkl', 'rb') as f:
#     data = pickle.load(f)

def transform_text(text):
    if text is None:
        return None
    true_values = {'true', 'yes', '1', '1.0', 1, 1.0}
    false_values = {'false', 'no', '0', '0.0', 0, 0.0}

    # Normalize value to string for consistent comparison
    str_text = str(text).strip().lower()

    # Check for boolean values
    if str_text in true_values:
        return True
    elif str_text in false_values:
        return False

    # Check if the text is a number
    if str_text.isdigit():
        return int(str_text)
    # Check if the text can be converted to a float
    try:
        return float(str_text)
    except ValueError:
        pass

    # Check if the text is a list
    if isinstance(text, str) and text.startswith('[') and text.endswith(']'):
        # Remove the surrounding brackets and split the content by commas
        elements = text[1:-1].split(',')
        # Strip whitespace and convert each element
        transformed_elements = [element.strip().strip('\'"') for element in elements]
        # Convert each element to a number if possible
        for i, elem in enumerate(transformed_elements):
            if elem.isdigit():
                transformed_elements[i] = int(elem)
            else:
                try:
                    transformed_elements[i] = float(elem)
                except ValueError:
                    pass
        # Sort the list after converting all elements to comparable types
        transformed_elements.sort(key=lambda x: float(x) if isinstance(x, (int, float, str)) and str(x).replace('.', '', 1).isdigit() else float('inf'))
        return transformed_elements

    # If not a number, list, or boolean, return as string
    return text

def get_most_common_answer(answers):
    # Transform each answer and handle unhashable types
    transformed_answers = []
    for ans in answers:
        transformed = transform_text(ans)
        # Convert lists to tuples to make them hashable
        if isinstance(transformed, list):
            transformed = tuple(transformed)
        transformed_answers.append(transformed)

    # Count occurrences of each transformed answer
    answer_counts = Counter(transformed_answers)

    # Return the most common answer
    most_common_answer = answer_counts.most_common(1)[0][0]
    return most_common_answer

# Initialize global counters
total_questions = 0
total_written_lines = 0
questions_not_found = 0

def compute_metrics(data, semeval_dev_qa, use_self_consistency=False):
    global total_questions, total_written_lines, questions_not_found
    # Initialize aggregate counters
    agg_n_bool = 0
    agg_n_list = 0
    agg_n_str = 0
    agg_n_num = 0

    agg_t_bool = 0
    agg_t_list = 0
    agg_t_str = 0
    agg_t_num = 0

    # Preprocess JSON data to create a question-to-subvalue mapping
    question_mapping = {}
    for key, sub_dict in data.items():
        for sub_key, sub_value in sub_dict.items():
            q = sub_value.get('question', '').strip()
            if q:
                question_mapping[q] = sub_value

    # Open a file to write the model answers
    with open('model_answers.txt', 'w') as answer_file:
        # Iterate through each example in semeval_dev_qa in order
        for idx, row in enumerate(semeval_dev_qa):
            question = row.get('question', '').strip()
            total_questions += 1

            # Retrieve the sub_value directly using the mapping
            sub_value = question_mapping.get(question, None)

            if sub_value:
                # Initialize variables
                model_answer = ""
                answer = ""
                sample_answer = ""

                # Extract model_answer, answer, and sample_answer from sub_value
                for k, v in sub_value.items():
                    if isinstance(v, float) and pd.isna(v):
                        # Handle NaN values by writing a blank line
                        model_answer = ""
                        break
                    if k.replace(" ", "").lower() in ['model_answers', 'model_answer']:
                        if v is None:
                            model_answer = ""
                        elif use_self_consistency and isinstance(v, list):
                            model_answer = get_most_common_answer(v)
                        else:
                            model_answer = transform_text(v.lower())
                    elif k.replace(" ", "").lower() == 'answer':
                        if v is None:
                            answer = ""
                        else:
                            answer = transform_text(v.lower())
                    elif k.replace(" ", "").lower() == 'sample_answer':
                        sample_answer = transform_text(v.lower())

                # Write the model_answer to the file (empty if not found)
                answer_file.write(str(model_answer) + '\n')
                total_written_lines += 1

                # Update type-specific counters based on sample_answer
                if isinstance(sample_answer, list):
                    agg_n_list += int(model_answer == answer)
                    agg_t_list += 1

                elif isinstance(sample_answer, str):
                    agg_n_str += int(model_answer == answer)
                    agg_t_str += 1

                elif isinstance(sample_answer, (int, float)):
                    agg_n_num += int(model_answer == answer)
                    agg_t_num += 1

                elif isinstance(sample_answer, bool):
                    agg_n_bool += int(model_answer == answer)
                    agg_t_bool += 1

            else:
                # If the question is not found in the JSON data, write a blank line
                answer_file.write('NULL\n')
                total_written_lines += 1
                # Optionally, you can log this event
                questions_not_found += 1
                print(f"Question not found: '{question}'")

            # Optionally, print progress every N questions
            if (idx + 1) % 100 == 0:
                print(f"Processed {idx + 1} questions...")

    # After processing all questions, calculate overall metrics
    print("\nAggregate Metrics:")
    if agg_t_bool > 0:
        print("  bool:", "{:.2f}%".format((agg_n_bool / agg_t_bool) * 100))
    if agg_t_str > 0:
        print("  str:", "{:.2f}%".format((agg_n_str / agg_t_str) * 100))
    if agg_t_num > 0:
        print("  num:", "{:.2f}%".format((agg_n_num / agg_t_num) * 100))
    if agg_t_list > 0:
        print("  list:", "{:.2f}%".format((agg_n_list / agg_t_list) * 100))
    total_types = agg_t_list + agg_t_bool + agg_t_num + agg_t_str
    total_correct = agg_n_list + agg_n_bool + agg_n_num + agg_n_str
    if total_types > 0:
        print("  Avg:", "{:.2f}%".format((total_correct / total_types) * 100))
    print()

# Load the semeval_dev_qa dataset
semeval_dev_qa = load_dataset("cardiffnlp/databench", name="semeval", split="dev")

# Call the function with the flag for self-consistency
compute_metrics(data, semeval_dev_qa, use_self_consistency=True)

print('Total questions:', total_questions)
print('Total written lines:', total_written_lines)
print('Total questions not found:', questions_not_found)
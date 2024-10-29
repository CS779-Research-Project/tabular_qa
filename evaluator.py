import pickle
import json
from collections import Counter

with open('results_gpt_dev.json', 'r') as f:
    data = json.load(f)

# with open('results/results_13b.pkl', 'rb') as f:
#     data = pickle.load(f)

# dump a json file with the data
# with open('results/results_7b_code2.json', 'w') as f:
#     json.dump(data, f, indent=4)

# assert False
# for k in data.keys():
#     print(k)

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
    if text.startswith('[') and text.endswith(']'):
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
        # This handles mixed types by converting all elements to floats for sorting
        transformed_elements.sort(key=lambda x: float(x) if isinstance(x, (int, float, str)) and str(x).replace('.', '', 1).isdigit() else float('inf'))
        return transformed_elements

    # If not a number, list, or boolean, return as string
    return text

# def compute_metrics(data):
#     # Initialize aggregate counters
#     agg_n_bool = 0
#     agg_n_list = 0
#     agg_n_str = 0
#     agg_n_num = 0

#     agg_t_bool = 0
#     agg_t_list = 0
#     agg_t_str = 0
#     agg_t_num = 0

#     # Iterate through each key in the data
#     for key, value in data.items():
#         n_bool = 0
#         n_list = 0
#         n_str = 0
#         n_num = 0

#         t_bool = 0
#         t_list = 0
#         t_str = 0
#         t_num = 0

#         # Process each sub_key and sub_value
#         for sub_key, sub_value in value.items():
#             model_answer = ""
#             answer = ""
#             sample_answer = ""
            
#             # Process each item within the sub_value dictionary
#             for k, v in sub_value.items():
#                 if type(v) == type(float('nan')):
#                     continue
#                 if k.replace(" ", "") == 'model_answer':
#                     if v is None:
#                         continue
#                     if type(v) == type(list()):
#                         print("List found in model_answer")
#                         assert False
#                     model_answer = transform_text(v.lower())
#                 if k.replace(" ", "") == 'answer':
#                     if v is None:
#                         continue
#                     answer = transform_text(v.lower())
#                 if k.replace(" ", "") == 'sample_answer':
#                     sample_answer = transform_text(v.lower())

#             # Check the type of sample_answer and update counters accordingly
#             if isinstance(sample_answer, list):
#                 n_list += int(model_answer == answer)
#                 t_list += 1

#             if isinstance(sample_answer, str):
#                 n_str += int(model_answer == answer)
#                 t_str += 1

#             if isinstance(sample_answer, (int, float)):
#                 n_num += int(model_answer == answer)
#                 t_num += 1

#             if isinstance(sample_answer, bool):
#                 n_bool += int(model_answer == answer)
#                 t_bool += 1

#         # Print metrics for the current key
#         print(f"Metrics for key: {key}")
#         if t_bool > 0:
#             print("  bool:", "{:.2f}%".format((n_bool / t_bool) * 100))
#         if t_str > 0:
#             print("  str:", "{:.2f}%".format((n_str / t_str) * 100))
#         if t_num > 0:
#             print("  num:", "{:.2f}%".format((n_num / t_num) * 100))
#         if t_list > 0:
#             print("  list:", "{:.2f}%".format((n_list / t_list) * 100))
#         if (t_list + t_bool + t_num + t_str) > 0:
#             print("  Avg:", "{:.2f}%".format((n_list + n_bool + n_num + n_str) / (t_list + t_bool + t_num + t_str) * 100))
#         print()

#         # Update aggregate counters
#         agg_n_bool += n_bool
#         agg_n_list += n_list
#         agg_n_str += n_str
#         agg_n_num += n_num

#         agg_t_bool += t_bool
#         agg_t_list += t_list
#         agg_t_str += t_str
#         agg_t_num += t_num

#     # Print aggregate metrics
#     print("Aggregate Metrics:")
#     if agg_t_bool > 0:
#         print("  bool:", "{:.2f}%".format((agg_n_bool / agg_t_bool) * 100))
#     if agg_t_str > 0:
#         print("  str:", "{:.2f}%".format((agg_n_str / agg_t_str) * 100))
#     if agg_t_num > 0:
#         print("  num:", "{:.2f}%".format((agg_n_num / agg_t_num) * 100))
#     if agg_t_list > 0:
#         print("  list:", "{:.2f}%".format((agg_n_list / agg_t_list) * 100))
#     if (agg_t_list + agg_t_bool + agg_t_num + agg_t_str) > 0:
#         print("  Avg:", "{:.2f}%".format((agg_n_list + agg_n_bool + agg_n_num + agg_n_str) / 
#                                          (agg_t_list + agg_t_bool + agg_t_num + agg_t_str) * 100))
#     print()

# compute_metrics(data)


# def get_most_common_answer(answers):
#     # Transform each answer and count the occurrences
#     transformed_answers = [transform_text(ans) for ans in answers]
#     answer_counts = Counter(transformed_answers)
#     # Return the most common answer
#     most_common_answer = answer_counts.most_common(1)[0][0]
#     return most_common_answer

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


def compute_metrics(data, use_self_consistency=False):
    # Initialize aggregate counters
    agg_n_bool = 0
    agg_n_list = 0
    agg_n_str = 0
    agg_n_num = 0

    agg_t_bool = 0
    agg_t_list = 0
    agg_t_str = 0
    agg_t_num = 0

    # Iterate through each key in the data
    for key, value in data.items():
        # if value if {}:
            # write 20 empty lines
            
        n_bool = 0
        n_list = 0
        n_str = 0
        n_num = 0

        t_bool = 0
        t_list = 0
        t_str = 0
        t_num = 0

        # Process each sub_key and sub_value
        for sub_key, sub_value in value.items():
            model_answer = ""
            answer = ""
            sample_answer = ""

            # Process each item within the sub_value dictionary
            for k, v in sub_value.items():
                if type(v) == type(float('nan')):
                    continue
                if k.replace(" ", "") == 'model_answers' or k.replace(" ", "") == 'model_answer':
                    if v is None:
                        continue
                    if use_self_consistency and isinstance(v, list):
                        # Get the most common answer from the list of model answers
                        model_answer = get_most_common_answer(v)
                    else:
                        # Process as single answer
                        model_answer = transform_text(v.lower())
                if k.replace(" ", "") == 'answer':
                    if v is None:
                        continue
                    answer = transform_text(v.lower())
                if k.replace(" ", "") == 'sample_answer':
                    sample_answer = transform_text(v.lower())

            # Check the type of sample_answer and update counters accordingly
            if isinstance(sample_answer, list):
                n_list += int(model_answer == answer)
                t_list += 1

            if isinstance(sample_answer, str):
                n_str += int(model_answer == answer)
                t_str += 1

            if isinstance(sample_answer, (int, float)):
                n_num += int(model_answer == answer)
                t_num += 1

            if isinstance(sample_answer, bool):
                n_bool += int(model_answer == answer)
                t_bool += 1

        # Print metrics for the current key
        print(f"Metrics for key: {key}")
        if t_bool > 0:
            print("  bool:", "{:.2f}%".format((n_bool / t_bool) * 100))
        if t_str > 0:
            print("  str:", "{:.2f}%".format((n_str / t_str) * 100))
        if t_num > 0:
            print("  num:", "{:.2f}%".format((n_num / t_num) * 100))
        if t_list > 0:
            print("  list:", "{:.2f}%".format((n_list / t_list) * 100))
        if (t_list + t_bool + t_num + t_str) > 0:
            print("  Avg:", "{:.2f}%".format((n_list + n_bool + n_num + n_str) / 
                                             (t_list + t_bool + t_num + t_str) * 100))
        print()

        # Update aggregate counters
        agg_n_bool += n_bool
        agg_n_list += n_list
        agg_n_str += n_str
        agg_n_num += n_num

        agg_t_bool += t_bool
        agg_t_list += t_list
        agg_t_str += t_str
        agg_t_num += t_num

    # Print aggregate metrics
    print("Aggregate Metrics:")
    if agg_t_bool > 0:
        print("  bool:", "{:.2f}%".format((agg_n_bool / agg_t_bool) * 100))
    if agg_t_str > 0:
        print("  str:", "{:.2f}%".format((agg_n_str / agg_t_str) * 100))
    if agg_t_num > 0:
        print("  num:", "{:.2f}%".format((agg_n_num / agg_t_num) * 100))
    if agg_t_list > 0:
        print("  list:", "{:.2f}%".format((agg_n_list / agg_t_list) * 100))
    if (agg_t_list + agg_t_bool + agg_t_num + agg_t_str) > 0:
        print("  Avg:", "{:.2f}%".format((agg_n_list + agg_n_bool + agg_n_num + agg_n_str) / 
                                         (agg_t_list + agg_t_bool + agg_t_num + agg_t_str) * 100))
    print()

# Call the function with the flag for self-consistency
compute_metrics(data, use_self_consistency=False)

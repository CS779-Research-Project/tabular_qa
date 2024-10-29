import json

# Sample JSON data (the input you provided)
with open('results_gpt_dev.json', 'r') as f:
    data = json.load(f)
# Default comparison function
def default_compare(value, truth, semantic=None):
    """ Default evaluation function. """
    return str(value).strip() == str(truth).strip()

# Variables to track evaluation
correct_count = 0
total_count = 0
model_outputs = []

# Evaluate the model
for key, entry in data.items():
    model_answer = entry["model_answer"]
    actual_answer = entry["answer"]
    
    # Compare using the default_compare function
    if model_answer is not None:
        comparison_result = default_compare(model_answer, actual_answer)
        if comparison_result:
            correct_count += 1
            
    # Increment the total count
    total_count += 1
    if model_answer is not None and model_answer != "":
        model_answer = model_answer.strip()
        output = model_answer.strip('[]')  # Remove brackets if present
    else:
        output = 'None'
    # Store model output, using 'None' if model_answer is missing
    model_outputs.append(output)

# Calculate accuracy
accuracy = correct_count / total_count if total_count > 0 else 0

# Output results
print(f"Accuracy: {accuracy:.2%}")

# Save model outputs to a file
with open('model_outputs.txt', 'w') as f:
    for output in model_outputs:
        f.write(f"{output}\n")

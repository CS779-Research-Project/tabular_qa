import outlines

examples = [
    ("The food was disgusting", "Negative"),
    ("We had a fantastic night", "Positive"),
    ("Recommended", "Positive"),
    ("The waiter was rude", "Negative")
]

@outlines.prompt
def labelling(to_label, examples):
    """You are a sentiment-labelling assistant.

    {% for example in examples %}
    {{ example[0] }} // {{ example[1] }}
    {% endfor %}
    {{ to_label }} //
    """

# model = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")
prompt = labelling("Just awesome", examples)
print(prompt)
# answer = outlines.generate.text(model)(prompt, max_tokens=100)
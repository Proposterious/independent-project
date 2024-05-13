"""Text utilities aka public functions for text verification/manipulation"""

def remove_punc(text: str) -> str:
    """Remove punctuation"""
    char_map = str.maketrans("", "", ".,!;:'")
    return text.translate(char_map)

def affirm(text: str) -> str:
    """Checks for affirmation"""

    # defines constant variables
    yes_responses = [
        "Affirmative",
        "Indeed",
        "Absolutely",
        "Certainly",
        "Definitely",
        "Without a doubt",
        "Of course",
        "Sure thing",
        "Yup",
        "Yeah",
        "Yes",
        "Yes we have"
    ]

    no_responses = [
        "Negative",
        "No",
        "Nope",
        "Nah",
        "Not at all",
        "Never",
        "Nuh-uh",
        "We haven't",
        "Sorry, we haven't",
        "I don't think so",
        "Unfortunately not",
        "Regrettably, no"
    ]

    for res in yes_responses:
        if res.lower().strip() in remove_punc(text.lower()).split(' '):
            print('positive')
            return 'positive'

    for res in no_responses:
        if res.lower().strip() in remove_punc(text.lower()).split(' '):
            print('negative')
            return 'negative'

    print(text.lower().split(' '))
    return "neither"

def trigger_exit(text: str) -> bool:
    """Returns True if User said 'quit' and False otherwise"""
    res = remove_punc(text.lower()).split(' ')

    for index, obj in enumerate(res):
        if obj == 'quit':
            print(f"{obj} found at index {index}")
            return True
    return False
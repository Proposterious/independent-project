"""Checks for affirmation"""

# defines constant variables
YES_RESPONSES = [
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

NO_RESPONSES = [
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

def compare(text: str) -> str:
    """returns a str ('affirmative', 'negative', 'neither')"""

    for res in YES_RESPONSES:
        if res.lower() in text.lower().split('.'):
            return 'positive'

    for res in NO_RESPONSES:
        if res.lower() in text.lower().split('.'):
            return 'negative'

    print(text.lower().split('.'))
    return "neither"


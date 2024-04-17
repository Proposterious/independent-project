"""Text utilities aka public functions for text verification/manipulation"""
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
        if res.lower() in text.lower().split('.'):
            return 'positive'

    for res in no_responses:
        if res.lower() in text.lower().split('.'):
            return 'negative'

    print(text.lower().split('.'))
    return "neither"

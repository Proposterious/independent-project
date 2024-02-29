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
    "Yeah"
]

no_responses = [
    "Negative",
    "No",
    "Nope",
    "Not at all",
    "Never",
    "Nuh-uh",
    "Sorry, we haven't",
    "I don't think so",
    "Unfortunately not",
    "Regrettably, no"
]

def compare(text: str) -> str:
    """returns a str ('affirmative', 'negative', 'neither')"""
    for pos_response in yes_responses:
        if pos_response in text:
            return 'affirmative'

    for neg_response in no_responses:
        if neg_response in text:
            return 'negative'

    return 'neither'

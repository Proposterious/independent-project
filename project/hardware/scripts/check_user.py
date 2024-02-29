'''Checks if User Exists'''

def askUser() -> bool:
    '''Returns bool dependant on verbal input'''
    # asks user if they exist
    answer: str = input("Have we met before? ")
    # process if input triggers in truthy dictionary
    return bool(answer)


# Notes
# - Replace bool(answer) with a way to check if verbal input
# is a type of affirmation such as "yes", "correct", "we have", etc.

'''Introduce User'''
# import interpret_response

def create_user() -> dict:
    '''create new user'''
    input_name: str = input("Well then, hello! My name is Storyelle." +
                       "What is your name? ")
    input_confirm: str = input("Should I call you by the name {input_name}? ")

    if bool(input_confirm):
        print("Okay then, {input_name}")
    else:
        input_name = input("What should I call you, instead? ")

    input_age = input("Before we continue, could you tell me how old you are? ")

    try:
        input_age = int(input_age)
    except TypeError:
        print("Okay!")

    input_dict = {
        "name": input_name,
        "age": input_age,
        "settings": ""
    }

    return input_dict

# Notes
# - Replace input() methods with a function that will
#   produce the question verbally and then process the
#   verbal response
# - Replace bool(answer) with a way to check if verbal input
# is a type of affirmation such as "yes", "correct", "we have", etc.
# - Replace print in 'except TypeError' with ways to check if user_age
# returned a written number, and if not then continue without age

def ask_user() -> bool:
    '''Returns bool dependant on verbal input'''
    # asks user if they exist
    answer: str = input("Have we met before? ")
    # process if input triggers in truthy dictionary
    return bool(answer)


# Notes
# - Replace bool(answer) with a way to check if verbal input
# is a type of affirmation such as "yes", "correct", "we have", etc.

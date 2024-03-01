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
        print("Thanks, {input_name}" )

    input_pref: str = input("When I refer to you with shorthand such as 'she went down the road'"
                            + " or 'he picked something up' what should I use?"
                            + "Since I am a girl, others refer to me by 'she'. ")

    input_age = input("Before we continue, could you tell me how old you are? ")

    # receive input_age as int or return 0
    try:
        input_age = int(input_age)
    except TypeError:
        input_age = 0

    input_dict = {
        "name": input_name,
        "age": input_age,
        "pref": input_pref,
        "settings": {
            "volume": 0,
            "voice": 0
        }
    }

    return input_dict

# Notes
# - Replace input() methods with a function that will
#   produce the question verbally and then process the
#   verbal response
# - Replace bool(answer) with a way to check if verbal input
# is a type of affirmation such as "yes", "correct", "we have", etc.
# - Replace int(input_age) with int([substring of input_age]) to check
# for first integer provided, ignoring other parts of the response.
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

'''Index File'''
import sys
import runtime

import introduction
import speech_handler
import user_class


power: bool = True

def start():
    '''sets up program'''
    if introduction.ask_user():
        # replace to await database
        print("user exists")
    else:
        introduction.create_user()

    loop()

def loop() -> bool:
    '''runs main program loop'''
    while power:
        # run main program
        print("running program")

    return False

# Global
# Replace input() with a method that takes two arguments.
# example: converse(robots_text, users_response)
# Replace print() with verbal response
# Check for profanity or inappropriate words for each response,
# preferably within whichever function interprets the speech

'''Index File'''
import user_class

import create_user
import check_user

power: bool = True

def start():
    '''sets up program'''
    if check_user.askUser():
        # replace to await database
        print("user exists")
    else:
        create_user.createUser()

    loop()

def loop() -> bool:
    '''runs main program loop'''
    while power:
        # run main program
        print("running program")
        
'''Index File'''
import introduction

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
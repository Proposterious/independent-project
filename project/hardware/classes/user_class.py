'''User Class'''
class User:
    '''Initiates User Class'''
    def __init__(self, name, age, settings) -> None:
        self.name = name
        self.age = age
        self.settings = settings

    def welcome_user(self) -> str:
        '''Welcomes the User'''
        return 'Welcome, {self.name}! Your recorded name is {self.age}'

    def grant_settings(self) -> None:
        '''Lists out the User's settings'''
        
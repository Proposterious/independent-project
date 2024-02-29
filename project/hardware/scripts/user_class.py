'''User Class'''
class User:
    '''Initiates User Class'''
    def __init__(self, name, age, settings) -> None:
        self.name: str = name
        self.age: int = age
        self.settings: dict = settings

    def welcome_user(self) -> str:
        '''Welcomes the User'''
        return 'Welcome, {self.name}! Your recorded name is {self.age}'

    def grant_settings(self) -> dict:
        '''Lists out the User's settings'''
        return 'Your settings are as follows... {self.settings}'

    def change_settings(self, key, value) -> dict:
        '''Changes settings based on input'''
        self.settings[key] = value
        return 'Your settings are as follows... {self.settings}'

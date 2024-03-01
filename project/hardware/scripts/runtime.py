"""Stores, Accesses Data that Exists in Runtime"""

def store_text(username: str, text: str) -> None:
    """Store text by username:str by username"""
    print("got username ", username)
    print("got text ", text)

    # write to stories.json
    print("stored text in stories.json")

def read_text(username: str) -> str:
    """Return story:str by Username"""
    # return text found in stories.json using the key 'username'
    print("found text by username ", username)

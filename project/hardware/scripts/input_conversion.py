"""Convert Speech Files (.wav) to String"""

def convert(path: str) -> str:
    """Grabs path to .wav file and converts to string"""
    # path should lead to audio file
    print("received the following speech\n", path)

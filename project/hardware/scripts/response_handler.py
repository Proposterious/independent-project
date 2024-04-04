import os
from os.path import join, dirname

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() # bring env variables in for os
myKey = os.environ(['OPENAI_KEY']) # grab openai api key

client = OpenAI(
    api_key = myKey
)

response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("sound/output.mp3")

"""ConversationManager Class"""
import os
import openai
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
load_dotenv() # bring env variables in for os

OPENAI_KEY = os.environ['OPENAI_API_KEY'] # grab api key
client = OpenAI(api_key=OPENAI_KEY) # initialize openai connection
class ConversationManager:
    """Manages User-ChatGPT communication"""
    def __init__(self, model_name="gpt-3.5-turbo-0125", ai_key = OPENAI_KEY, voice = "nova"):
        # Initialize OpenAI API with model
        self.voice = voice
        self.ai_key = ai_key
        self.model_name = model_name

    def respond(self, user_input: list) -> str:
        """Generate response using OpenAI API"""

        response = client.chat.completions.create(
            model = self.model_name,
            response_format = { "type": "json_object" },
            messages = [
                user_input
            ]
        )
        return response.choices[0].text.strip()

    def create_speech(self, text, path: str) -> bool:
        """Convert text to speech and save to file with 'path'"""

        speech_file_path = Path(__file__).parent.parent / "sound" / path
        response = openai.audio.speech.create(
            model="tts-1",
            voice=self.voice,
            input=text,
            response_format="wav"
        )

        response.with_streaming_response.method(speech_file_path)

    def transcribe_speech(self, path) -> bool:
        """Convert speech to text accessed with 'path'"""

        audio_file = open(path, "rb")
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

        if transcript:
            return True
        return False
    # Other methods for conversation management...

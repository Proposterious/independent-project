"""ConversationManager Class"""
import os
import time
import openai
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
load_dotenv() # bring env variables in for os

OPENAI_KEY = os.environ['OPENAI_API_KEY'] # grab api key
client = OpenAI(api_key=OPENAI_KEY) # initialize openai connection
class ConversationManager:
    """Manages User-ChatGPT communication"""
    def __init__(self, assistant: str, model_name="gpt-4.0-turbo", ai_key = OPENAI_KEY, voice = "nova"):
        # Initialize OpenAI API with model
        self.voice = voice
        self.ai_key = ai_key
        self.assistant = assistant
        self.model_name = model_name

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

    def respond(self, thread_id: str, user_input: str) -> str:
        """Generate response using OpenAI API"""
        if thread_id:
            thread = client.beta.threads.retrieve(thread_id)
        else:
            thread = client.beta.threads.create()
        try:
             client.beta.threads.messages.create(
                thread_id = thread_id,
                role = "user",
                content = user_input
            )
        except Error as e: # pylint: disable=undefined-variable
            print(f"Received error {e}, Failure")

        run = client.beta.threads.runs.create(
            thread_id = thread.id,
            assistant_id = self.assistant
        )

        while run.status in ("queued", "in_progress"):
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id,
            )
            time.sleep(0.25)

        messages = client.beta.threads.messages.list(
            thread_id = thread_id
        )

        # self.create_speech(messages.data[0].content[-1].text.value, "latest_response.wav")

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

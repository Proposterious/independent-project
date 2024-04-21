"""ConversationManager Class"""
import os
import time
import openai
import whisper
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
from playsound import playsound
from utils.text_utils import affirm
from utils.file_utils import record_audio

load_dotenv() # bring env variables in for os

OPENAI_KEY = os.environ['OPENAI_API_KEY'] # grab api key
client = OpenAI(api_key=OPENAI_KEY) # initialize openai connection

PARENT_PATH = Path(__file__).parent

class ConversationManager:
    """Manages User-ChatGPT communication"""
    def __init__(self, assistant: str, model_name="gpt-4.0-turbo", voice = "nova"):
        # Initialize OpenAI API with model
        self.voice = voice
        self.assistant = assistant
        self.model_name = model_name

    def create_speech(self, text, path: str) -> bool:
        """Convert text to speech and save to file with 'path'"""
        speech_file_path = PARENT_PATH / "sound" / path
        response = client.audio.speech.create(
            model="tts-1",
            voice=self.voice,
            input=text,
            response_format="wav"
        )

        response.stream_to_file(speech_file_path)

        if response:
            return True
        else:
            return False

    def transcribe_speech(self, path) -> str | bool:
        """Convert speech to text accessed with 'path'"""
        speech_file_path = f"{Path(__file__)} / sound / {path}"
        audio_file = open(speech_file_path, "rb")
        transcription = openai.audio.transcriptions.create(
            model="whisper-1",
            format="wav",
            file=audio_file
        )

        if transcription:
            return transcription.text
        return False
    
    def beep(self):
        """Play a beep to signal to user that the robot is finished speaking"""
    # Functions that Interact with User
    def introduce_user(self):
        """Introduce the User to VISoR"""
        introduce_path = os.path.dirname(__file__) + "\sound\introduceUser.mp3"
        playsound(introduce_path)
        
        


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
            thread_id = thread_id,
            assistant_id = self.assistant
        )

        while run.status in ("queued", "in_progress"):
            run = client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id,
            )
            time.sleep(0.25)

        messages = client.beta.threads.messages.list(
            thread_id = thread.id
        )

        # self.create_speech(messages.data[0].content[-1].text.value, "latest_response.wav")

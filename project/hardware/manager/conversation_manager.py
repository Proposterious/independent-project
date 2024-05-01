"""ConversationManager Class"""
import os
import time
import whisper
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
from playsound import playsound
from utils.text_utils import affirm
from utils.file_utils import record_audio

load_dotenv() # bring env variables in for os

OPENAI_KEY = os.environ['OPENAI_API_KEY'] # grab api key
client = OpenAI(api_key=OPENAI_KEY) # initialize openai connection

PARENT_PATH = Path(__file__).parent
FAILED_RES_PATH = f"{Path(__file__).parent}\\sound\\noResponse.mp3"

class ConversationManager:
    """Manages User-ChatGPT communication"""
    def __init__(self, assistant: str, model_name="gpt-4.0-turbo", voice = "nova"):
        # Initialize OpenAI API with model
        self.voice = voice
        self.assistant = assistant
        self.model_name = model_name

    def beep(self): #in-progress
        """Play a beep to signal to user that the robot is finished speaking"""

    def create_speech(self, text, path: str, format_type: str) -> None:
        """Convert text to speech and save to file with 'path'"""
        speech_file_path = PARENT_PATH / "sound" / path
        response = client.audio.speech.create(
            model="tts-1",
            voice=self.voice,
            input=text,
            response_format=format_type
        )

        response.stream_to_file(speech_file_path)

    def transcribe_speech(self, path) -> str | bool:
        """Convert speech to text accessed with 'path'"""
        speech_file_path = f"{PARENT_PATH}\sound\{path}"

        model = whisper.load_model("base")
        result = model.transcribe(speech_file_path)

        return result["text"]

    def failed_response(self):
        """ Alerts user that their request failed """
        playsound(FAILED_RES_PATH)
   
    # Functions that Interact with User
    def introduce_user(self):
        """Introduce the User to VISoR"""
        introduce_path = os.path.dirname(__file__) + "\sound\introduceUser.mp3"
        playsound(introduce_path)

        # Get user's response as transcription
        record_audio()
        transcription = self.transcribe_speech("latestFile.wav")
        affirmation = affirm(transcription)
        return bool(affirmation == "positive")

    def get_name(self):
        """Asks user for name and then awaits response"""
        ask_user_path = f"{PARENT_PATH}\\sound\\askUser.mp3"
        playsound(ask_user_path)

        # Get user's response as transcription
        record_audio()
        transcription = self.transcribe_speech("latestFile.wav")

        print(transcription)
        return transcription.lower().strip()

    def new_user(self):
        """Introduce the User to VISoR"""
        welcome_path = os.path.dirname(__file__) + "\\sound\\firstUse.mp3"
        playsound(welcome_path)

        # Get user's response as transcription
        record_audio()
        transcription = self.transcribe_speech("latestFile.wav")
        user_name = transcription.lower().strip()
        return user_name

    def begin_session(self) -> str:
        """Ask user if they would like to begin the session"""
        begin_session_path = os.path.dirname(__file__) + "\\sound\\beginSession.mp3"
        playsound(begin_session_path)

        # Get user's response as transcription
        record_audio()
        transcription = self.transcribe_speech("latestFile.wav")
        affirmation = affirm(transcription)
   
        if bool(affirmation == "positive"):
            return "yes"
        elif affirmation == "neither":
            self.failed_response()
            self.begin_session()
        return "no"
        # Get user's response as transcription

    def prev_sessions(self, stories: list) -> str:
        """ Return and return past sessions """
        temp_path = f"{PARENT_PATH}\\sound\\prevStory.wav"
        question = "I will list out stories from our previous sessions."
        for story in range (0, len(stories)-1):
            question += f"{story}) {stories[story].title}"
            print(f"Found {stories[story]}")

        self.create_speech(question, temp_path, 'wav')
        record_audio()
        transcription = self.transcribe_speech("latestFile.wav")
        for res in transcription.lower().split():
            try:
                chosen_story = int(res)
                return chosen_story
            except ValueError:
                pass

        return chosen_story

    def user_response(self) -> str:
        """ Gets user's input as transcription """
        record_audio()
        transcription = self.transcribe_speech("latestFile.wav")
        return transcription

    def assistant_response(self, user_input: str, thread_id: str) -> str:
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
        except Exception as e: # pylint: disable=undefined-variable
            print(f"Received error {e}, Failure")
            return

        run = client.beta.threads.runs.create(
            thread_id = thread_id,
            assistant_id = self.assistant
        )

        while run.status in ("queued", "in_progress"):
            run = client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id,
            )
            time.sleep(0.15)

        messages = client.beta.threads.messages.list(
            thread_id = thread.id
        )

        self.create_speech(messages.data[0].content[-1].text.value, "latestFile.wav", "wav")

        playsound(f"{PARENT_PATH}\\sound\\latestFile.wav")

        return messages[-1].content[0].text.value
"""Handles Background Music during Runtime"""
import os
import time
import threading
from openai import OpenAI
from utils.file_utils import read_assistants
from pydub import AudioSegment, playback

OPENAI_KEY = os.environ['OPENAI_API_KEY'] # grab api key
client = OpenAI(api_key=OPENAI_KEY) # initialize openai connection

MUSIC_DICT = {
    "terrifying": "in-a-dark-cave-rage-sound.mp3",
    "mysterious": "abandoned-factor-finval.mp3",
    "victorious": "another-world-dima-tyshko.mp3",
    "futuristic": "elysium-victor-cooper.mp3",
    "adventurous": "safari-victorwayne.mp3",
    "country_side": "hometown-air-edrecords.mp3",
    "silent_travel": "mountain-landscape-pillowvibes"

}
MUSIC_PATH = os.path.dirname(__file__) + "\\sound\\music\\"

STORYTELLERS = read_assistants()
MUSICIAN_ASSISTANT = STORYTELLERS["Musician"]

class MusicManager:
    """Manages Background Music"""
    def __init__(self):
        self.ref = None
        self.play_obj = None
        self.lock = threading.Lock()
        # initialize thread
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def set_ref(self, ref: str):
        """update ref to music file"""
        self.ref = MUSIC_DICT[ref]

    def musician_response(self, message: str) -> str:
        """Generate response using OpenAI API"""
        thread = client.beta.threads.create()

        try: # create thread w/ musician
            client.beta.threads.messages.create(
                thread_id = thread.id,
                role = "user",
                content = message
            )

        except Exception as e: # pylint: disable=undefined-variable
            print(f"Received error {e}, Failure")
            return

        run = client.beta.threads.runs.create(
            thread_id = thread.id,
            assistant_id = MUSICIAN_ASSISTANT
        )

        while run.status in ("queued", "in_progress"):
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id,
            )
            time.sleep(0.15)

        messages = client.beta.threads.messages.list(
            thread_id = thread.id
        )

        # update ref w/ new message
        self.ref(messages.data[0].content[-1].text.value)
 
    def run(self):
        """loop main method"""
        current_song = None
        while True:
            with self.lock:
                if current_song != self.ref:
                    # stop music if playing
                    try:
                        self.play_obj.stop()
                    except Exception:
                        continue
                    
                    # play music from updated ref
                    current_song = self.ref
                    file = AudioSegment.from_mp3(file = MUSIC_PATH + self.ref)
                    self.play_obj = playback._play_with_simpleaudio(file)
                    print("changed playback object")

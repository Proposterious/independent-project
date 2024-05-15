"""Handles Background Music during Runtime"""
import os
import threading
from pydub import AudioSegment, playback

MUSIC_DICT = {
    "spooky": "in-a-dark-cave-rage-sound.mp3",
    "mysterious": "abandoned-factor-finval.mp3",
    "victorious": "another-world-dima-tyshko.mp3",
    "futuristic": "elysium-victor-cooper.mp3",
    "adventurous": "safari-victorwayne.mp3",
    "country_side": "hometown-air-edrecords.mp3",
    "silent_travel": "mountain-landscape-pillowvibes"

}
MUSIC_PATH = os.path.dirname(__file__) + "\\sound\\music\\"

class MusicManager:
    """Manages Background Music"""
    def __init__(self):
        self.ref = None
        self.play_obj = None
        # initialize thread
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def set_ref(self, ref: str):
        """update ref to music file"""
        self.ref = MUSIC_DICT[ref]

    def run(self):
        """loop main method"""
        current_song = None
        while True:
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


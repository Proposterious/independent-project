"""File utilities aka public functions for file verification/animation"""
import wave
import time
import json
import contextlib
from pathlib import Path

import ffmpeg
import pyaudio
import keyboard


def record_audio():
    """Record and Save Audio"""
    FORMAT = pyaudio.paInt16
    CHANNELS = 1

    RATE = 44100
    CHUNK = 1024
    OUTPUT_FILENAME = f"{Path(__file__).parent.parent}\sound\latestFile.wav"

    print(OUTPUT_FILENAME)
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    frames = []
    print("Press SPACE to start recording.")
    keyboard.wait('space')
    print("Recording... Press SPACE to stop.")
    time.sleep(0.2)

    while True:
        try:
            data = stream.read(CHUNK)
            frames.append(data)
        except KeyboardInterrupt:
            break
        
        if keyboard.is_pressed('space'):
            print("stopping recording after a brief delay...")
            time.sleep(0.1)
            break

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

def find_length(file_path, file_type: str):
    """Returns duration of an audio file"""
    if file_type == "wav":
        with contextlib.closing(wave.open(file_path,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            print(duration)
    else:
        duration = ffmpeg.probe(file_path)['format']['duration']

    return duration

def read_users() -> dict:
    """Returns Users from 'users.json' as dict"""
    users_path = Path(__file__).parent.parent.parent / "json" / "users.json"

    with open(users_path, "r", encoding="utf-8") as json_file:
        users = json.load(json_file)
        return users

def get_specified_user(username: str) -> dict:
    """Returns Specified User as 'dict' object"""
    users = read_users()
    return users[username]

def read_assistants() -> dict:
    """Returns Storytellers from 'storytellers.json' as dict"""
    storytellers_path = Path(__file__).parent.parent.parent / "json" / "storytellers.json"

    with open(storytellers_path, "r", encoding="utf-8") as json_file:
        storytellers = json.load(json_file)
        return storytellers

"""File utilities aka public functions for file verification/animation"""
import wave
import time
import ffmpeg
import pyaudio
import keyboard
import contextlib
from pathlib import Path

def record_audio():
    """Record and Save Audio"""
    FORMAT = pyaudio.paInt16
    CHANNELS = 1

    RATE = 44100
    CHUNK = 1024
    OUTPUT_FILENAME = Path(__file__).parent / "sound" / "latestFile.wav"

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
            time.sleep(0.2)
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
    if file_type == "wav":
        with contextlib.closing(wave.open(file_path,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            print(duration)
    else:
        duration = ffmpeg.probe(file_path)['format']['duration']

    return duration

file_path = Path(__file__).parent / "sound" / "latestFile.wav"
file_type = "wav"

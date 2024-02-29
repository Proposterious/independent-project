"""Converts speech (.wav) files to text"""
import whisper

model = whisper.load_model("base")
model.transcribe("idioms.wav")

def convert_speech(text) -> str:
    text
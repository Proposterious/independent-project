"""Converts speech (.wav) files to text"""
import whisper

model = whisper.load_model("base")

async def convert_speech(text) -> str:
    """
    handles speech-to-text conversion

    text: path to audio file
    """
    
    text = await model.transcribe(text)
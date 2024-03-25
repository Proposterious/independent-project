"""Converts speech (.wav) files to text"""
import whisper

MODEL = whisper.load_model("base")

def interpret_speech(path: str) -> str:
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the MODEL
    mel = whisper.log_mel_spectrogram(audio).to(MODEL.device)

    # detect the spoken language
    _, probs = MODEL.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(MODEL, mel, options)

    # print the recognized text
    print(result.text)

async def convert_speech(path: str) -> str:
    """
    handles speech-to-text conversion

    path: path to audio file
    """
    
    text = await MODEL.transcribe(path)

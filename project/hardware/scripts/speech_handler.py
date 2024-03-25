"""Converts speech (.wav) files to text"""
import whisper

Model = whisper.load_model("base")

def interpret_speech(path: str) -> str:
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(path)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the Model
    mel = whisper.log_mel_spectrogram(audio).to(Model.device)

    # detect the spoken language
    _, probs = Model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(Model, mel, options)

    # print the recognized text
    print(result.text)

async def convert_speech(path: str) -> str:
    """
    handles speech-to-text conversion

    path: path to audio file
    """
    
    text = await Model.transcribe(path)

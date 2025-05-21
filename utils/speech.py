import speech_recognition as sr
from gtts import gTTS
import os

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"📝 You said: {text}")
        return text
    except Exception as e:
        print("❌ Error:", e)
        return ""

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    filename = "response.mp3"
    tts.save(filename)
    os.system(f"start {filename}" if os.name == 'nt' else f"mpg123 {filename}")
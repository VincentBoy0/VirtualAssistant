# import pyttsx3

# def textToAudio(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait() 

from gtts import gTTS
import os
import playsound

def textToAudio(text, myLang = "en"):
    tts = gTTS(text = text, lang = myLang)
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

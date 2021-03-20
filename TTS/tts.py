import pyttsx3
from gtts import gTTS
import os


def tts(text):
    engine = pyttsx3.init()
    engine.say('This is a text')
    engine.runAndWait()
    voices = engine.getProperty('voices')
    for v in range(len(voices)):
        engine.setProperty('voice', voices[v].id)
        engine.say('I am voice number,' + str(v))
    engine.runAndWait()

def text_to_speech(file_path):

    file = file_path
   
    f = open(file, 'r+')
    text = f.read()
    tts = gTTS(text=text, lang='en')

    tts.save("test.mp3")

#text_to_speech("out_text.txt")
tts('geri')
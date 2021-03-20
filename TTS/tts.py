from gtts import gTTS
import os

def text_to_speech(file_path):

    file = file_path
   
    f = open(file, 'r+')
    text = f.read()
    tts = gTTS(text=text, lang='en')

    tts.save("test.mp3")

text_to_speech("out_text.txt")
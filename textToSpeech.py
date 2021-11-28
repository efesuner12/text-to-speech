from gtts import gTTS
from playsound import playsound
import os

text = str(input("Please enter the text you want to convert: "))

language = 'en'

myobj = gTTS(text=text, lang=language, slow=False)

filename = "speech1.mp3"
myobj.save(filename)

playsound(filename, True)

os.remove(filename)

from gtts import gTTS
import os

language = "en"

Text = raw_input("Text: ")

myobj = gTTS(text=Text,lang=language)

myobj.save("welc.mp3")

os.system("mpg123 welc.mp3")


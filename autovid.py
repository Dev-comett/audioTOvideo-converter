import moviepy.editor
from tkinter.filedialog import *
import random

num = round(random.random()*10)

vid=askopenfilename()
video=moviepy.editor.VideoFileClip(vid)

aud=video.audio

fileName = f"audio{num}.mp3" 
aud.write_audiofile(fileName)
print("conversion successfully")
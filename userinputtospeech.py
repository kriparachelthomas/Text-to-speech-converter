from gtts import gTTS
import os
from tkinter import *
root = Tk()
canvas= Canvas(root,width=400,height=300)
canvas.pack()
def texttospeech():
    text=entry.get()
    output = gTTS(text=text, lang='en', slow=False)
    output.save('useroutput.mp4')
    os.system('start useroutput.mp4')
entry= Entry(root)
canvas.create_window(200,100,window=entry)
button=Button(text="start",command=texttospeech)
canvas.create_window(200,230,window=button)
root.mainloop()

from gtts import gTTS
import os
text=open('hi.txt','r').read()
output=gTTS(text=text,lang='en',slow=False)
output.save('fileoutput.mp3')
os.system('start fileoutput.mp3')
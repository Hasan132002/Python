import tkinter as tk
from gtts import gTTS
from playsound import playsound
win=tk.Tk()
win.title('TEXT TO SPEECH')
win.geometry('200x70')
def text_to_speech():
    text=entry.get()
    speech=gTTS(text=text,lang='ur')
    speech.save(r'1.mp3')
    playsound(r'1.mp3')
l=tk.Label(win,text='ENTER HERE : ')
l.grid(row=0,column=0)
entry=tk.Entry(win)
entry.grid(row=1,column=0)
b=tk.Button(win,text='GO',command=text_to_speech)
b.grid(row=1 ,column=1)
win.mainloop()
    
import tkinter as tk
from googletrans import Translator
window=tk.Tk()
window.title('Translator')
window.geometry('200x70')
def translation():
    word=root.get()
    translator=Translator(service_urls=['translate.google.com'])
    translations=translator.translate(word,dest='ur')
    l1=tk.Label(window,text=f'Translated in Urdu:{translations.text}',bg='yellow')
    l1.grid(row=2,column=0)
l=tk.Label(window,text='Enter Word : ')
l.grid(row=0 ,column=0,sticky='W')
root=tk.Entry(window)
root.grid(row=1,column=0)
window.geometry('300x300')
button=tk.Button(window,text='Translate',command=translation)
button.grid(row=1,column=2)
window.mainloop()
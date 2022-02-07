'''import tkinter as tk
from tkinter import *
from tkinter import ttk

class karl( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Karlos")
        self.button1 = Button( self, text = "CLICK HERE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    def new_window(self):
        self.newWindow = karl2()
class karl2(Frame):     
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("karlos More Window")
        new.button = tk.Button(  text = "PRESS TO CLOSE", width = 25,
                                 command = self.close_window )
        new.button.pack()
    def close_window(self):
        self.destroy()
def main(): 
    karl().mainloop()
if __name__ == '__main__':
    main()
from tkinter import*
import wifi as w
s=Tk()
button = Button(s, text = "Click Me",command=w).pack()
'''
#from wifi import kk as w
'''from tkinter import*
def kk():
    import subprocess
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<40}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<40}|  {:<}".format(i, ""))



g=Tk()
s=Button(g,text='Click me',command=kk).pack()
'''
'''from tkinter import*
def s():
    t.delete(0.0,'end')
    tn=ent.get()
    g=vv.get()
    print(tn,g)
    s=(str(tn)+'how are you')
    t.insert(0.0,tn)
g=Tk()
g.geometry=('200x250')
#ent=Entry(g)
l=Label(g,text='Name : ')
l1=Label(g,text='Gender : ')
ent=Entry(g)
vv=IntVar()
r=Radiobutton(g,text='Male',variable=vv,value=1)
r1=Radiobutton(g,text='feMale',variable=vv,value=2)
l.grid(row=0)
l1.grid(row=1)
ent.grid(row=0,column=1)
r.grid(row=1,column=1,sticky=W)
r1.grid(row=1,column=1,sticky=E)
b=Button(g,text='kk',command=s)
b.grid(row=2,columnspan=2)
t=Text(g,width=25,height=10,wrap=WORD)
t.grid(row=3,columnspan=2,sticky=W)
g.mainloop()
'''
'''from tkinter import*
from wifi import kk 
def get_it():
    entry_value=entry.get()
    answer_value=kk()(entry_value)
    answer.insert(INSERT,answer_value)
root=Tk()
topframe=Frame(root)
entry=Entry(topframe)
entry.pack()
button=Button(topframe,text="search",command=get_it)
button.pack()
topframe.pack(side=TOP)
bottonframe=Frame(root)
scroll=Scrollbar(bottonframe)
scroll.pack(side=RIGHT,fill=Y)
answer=Text(bottonframe,width=40,height=10,yscrollcommand=scroll.set,wrap=WORD)
answer.pack()
bottonframe.pack()
root.mainloop()
'''
import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<40}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<40}|  {:<}".format(i, ""))








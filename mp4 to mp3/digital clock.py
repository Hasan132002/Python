from tkinter import*
import time
def times():
    c=time.strftime('%I:%M:%S:%p')
    c=Label(root,font='chiller 80',bg='white',fg='black',text=c)
    c.after(200,times)
    c.grid(row=0,column=1)
root=Tk()
root.title('Digital Clock')
root.resizable(False,False)
times()
root.mainloop()
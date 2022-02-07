import tkinter
from tkinter import*    
def kk():
#First import subprocess, this is the module we will use to interact with the cmd.
    import subprocess
#Next, get the output for the command "netsh wlan show profiles" using subprocess.check_output().
#Then decode the output with utf-8 and split the string by a newline character to get each line in a separate string.
    data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-16',errors='backslashreplace').split('\n')
#We have a list of strings, we can get lines that only contain "All User Profile".
#With these lines we then need to split it by a ':', get the right hand side and remove the first and last character
    profiles=[i.split(':')[1][1:-1] for i in data if 'All User Profile'in i]
#Now that the variable a contains the WiFi profile names, we can get the output for the command "netsh wlan show profile {Profile Name}key=clear“
#using subprocess.check_output() again for a particular profile while looping through all profiles.   
    for i in profiles:
        try:
            results=subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8',errors='backslashreplace').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#Now we should have a list containing one string which is the particular profiles key.
#Here you could just use a simple print statement but I have just formatted it a bit.
#Now put a input call at the end of the script outside the loop so that when the script is run it will not immediately stop when results are displayed.
            try:
                print('{:<30}| {:<}'.format(i,results[0]))
            except IndexError:
                print("{:<30}| {:<}".format(i, ""))
        except subprocess.CalledProcessError:
            print('{:<30}| {:<}'.format(i,'ENCODING ERROR'))
#Now making a button whenever you click on the button its will gives you an output
root=tkinter.Tk()
#Giving title
root.title("Get Wifi Password")
#Its will fix the size of the window
root.resizable(width=False, height=False)
#Height and width
root.geometry('600x350')
#Putting Image on Button
photo=PhotoImage(file='3.png')
#Title
label_display =Label(root, text="Click On the Image to get built-in Password",font=('chiller',30,'bold')).grid()
#Button
btn=Button(root,image=photo,command=kk,border=0,height=300,width=350).place(x=80,y=50)


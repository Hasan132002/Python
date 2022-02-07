'''import keyboard
while True:
    key=keyboard.read_key()
    print(keyppakistan)
    if keyboard.read_key()=='esc':
        break
'''
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('hasanraza132002@gmail.com','password')
msg='HA BHAI KIA HAL HA TMHARA'
server.sendmail('hasanraza132002@gmail.com','hamzamehboob105@gmail.com',msg)
print('Mail Sent')
server.quit()
                    
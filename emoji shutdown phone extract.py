#shut down
#import os
#def shutdown():
 #   os.system('shutdown /s /t')
#shutdown()
#phone number extract
#import re
#p=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#m=p.search('my number 345-543-5678.')
#print('Phone number found :'  + m.group())
from emoji import emojize
print(emojize(':bus: :house:'))
print(emojize(':phone:',use_aliases=True))



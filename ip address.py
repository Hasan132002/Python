import socket
print('y/n')
r=input()
if r=='n':
    exit()
else:
    print('Your IP address is',end='')
    print(socket.gethostbyname(socket.gethostname()))

'''def hcf(x,y):
    while (y):
        x, y = y,x % y
    return x
k=input('enter')
l=input('enter')
hcf=hcf(30,400)
print('H.C.F is',hcf)
'''
'''import nmap
#from getmac import get_mac_address
class network(object):
    def __init__(self):
        ip=input("Enter IP that are default")
        self.ip=ip
    #def __get_mac(self,IP='192.168.56.1'):
        #mac =get_mac_address(IP)
        #return mac
    def networkscanners(self):
        if len(self.ip)==0:
            network='192.168.1.1/24'
        else:
            network=self.ip+'/24'
            
        print('Scanning Please wait')
        nm=nmap.PortScanner()
        nm.scan(hosts=network,arguments='-sn')
        hosts_list=[(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host,status in hosts_list:
            #mac=self.__get_mac(IP=host)
            print('Host\t{}'.format(host))
#if __name__ == '__main__ ':
D=network()
D.networkscanners()
        
'''
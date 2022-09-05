from socket import gethostbyname
from sys import exit



def start():
    print('\nIpDectecta is a Penetration testing tool brought to you by wale,\nipDetecta helps to get the ip address of a target or client that is undergoing a penetration test through it`s hostname.\n')
    while True:
        hostName=str(input('input the hostname e.g www.google.com: '))
        if hostName != 'quit':
            try:  
                print(gethostbyname(hostName))
            except: 
                print('invalid input !!')
        else:
            exit()



if __name__ == '__main__':
    start()


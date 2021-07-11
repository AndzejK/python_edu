#A simple browaser
import socket
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80)) #connect to/ extend the connection to. Like a phone call
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #we sending here bites Not string
mysock.send(cmd)

while True:
    data=mysock.recv(512) #512 means up to 512 characters at a time
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()
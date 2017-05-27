import socket


s = socket.socket()
host = '192.168.42.1'
port = 12345

s.connect((host, port))
print('connected')
a = input('a=')
b = input('b=')
s.send(int(a))
s.send(int(b))
c = int(s.recv(1024))
print(c)

s.close
print('connection closed')

 

import socket

s = socket.socket()
#host = '192.168.42.1'
host = socket.gethostname()
port = 12345

s.connect((host,port))
print('>>>>connected')

s.send('message from client'.encode())

data = s.recv(1024).decode()
print(data)
s.close
print('connection closed')




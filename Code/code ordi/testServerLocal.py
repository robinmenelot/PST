import socket

s = socket.socket()

host = socket.gethostname()
port = 12345

s.bind((host,port))
s.listen(5)

isServerOpen = True

while isServerOpen == True:
	c, addr = s.accept()
	print('connected')
	data = ''
	data = c.recv(1024).decode()
	print(data)
	c.send('message from server'.encode())
	c.close()
	isServerOpen = False

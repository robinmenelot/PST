import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)

isServerOpen = True
while isServerOpen == True:
	c1, adrss1 = s.accept()
	print(adrss1,' connected')
	c2, adrss2 = s.accept()
	print(adrss2, 'connected')
	print('yolo')
	c1.send('bye'.encode())
	c2.send('bye'.encode())
	c1.close()
	c2.close()
	self.socket.close()
	isServerOpen = False



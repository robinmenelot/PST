import socket
from Getch import Getch

if __name__ == '__main__':

	s = socket.socket()
	host = '192.168.42.1'
	port = 8087
	s.bind((host,port))
	s.listen(5)

	isServerOpen = True
	data = ''
	c1, adrss1 = s.accept()
	print(adrss1,' connected')

	while isServerOpen==True:
		first = Getch()()
		if first == 'q':
			c1.send('q'.encode())
			c1.close()
			s.close()
			isServerOpen = False
		elif first == '\033':
			Getch()()
			key = Getch()()
			if key=='A':
				print('up')
				c1.send('up'.encode())
			if key=='B':
				print('down')
				c1.send('down'.encode())
			if key=='C':
				print('right')
				c1.send('right'.encode())
			if key=='D':
				print('left')
				c1.send('left'.encode())

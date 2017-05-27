import socket
import time
from Getch import Getch,whatKeyIsPressed

if __name__ == '__main__':
	
	s = socket.socket()
	host = '192.168.42.1'
	port = 8087
	s.connect((host,port))
	
	while True:
		time.sleep(0.1)
		key = whatKeyIsPressed()
		s.send(key.encode())
		print(key)
		if key == 'q':
			s.close()
			break


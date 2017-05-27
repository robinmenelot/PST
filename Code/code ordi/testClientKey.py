import socket
import ev3dev.ev3 as ev3
import time

s = socket.socket()
host = '192.168.42.1'
#host = socket.gethostname()
port = 12345
s.connect((host,port))
print('connect to host')

mA = ev3.LargeMotor('outA')

while True:
	data = s.recv(1024).decode()
	print(data)
	if data == 'q':
		s.close()
		break
	if data == 'up':
		print('UP')
		mA.run_timed(time_sp=1000, speed=300)
	if data == 'down':
		print('DOWN')
		mA.run_timed(time_sp=1000, speed=-300)

class Getch:
	def __init__(self):
		import tty, sys

	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

def whatKeyIsPressed () :
	while True:
		init = Getch()()
		if init == 'q':
			return 'q'
			break
		if init == 'z':
			return 'z'
		if init == 's':
			return 's'
		elif init == '\033':
			Getch()()
			key = Getch()()
			if key=='A':
				return 'up'
			if key=='B':
				return 'down'
			if key=='C':
				return 'right'
			if key=='D':
				return 'left'

from Getch import Getch

if __name__ == '__main__':
	while True:
		if Getch()() == '\033':
			if Getch()() == 'q':
				break		
			else:
				key = Getch()()			
				if key=='A':
					print('UP')
				if key=='B':
					print('DOWN')
				if key=='C':
					print('RIGHT')
				if key=='D':
					print('LEFT')
					break
				if key==ord('q'):
					print('quit')


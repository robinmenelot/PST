from Getch import Getch

if __name__ == '__main__':
        while True:
                first = Getch()()
                if first == 'q':
                        break;
                elif first == '\033':
                        Getch()()
                        key = Getch()()
                        if key=='A':
                                print('up')
                        if key=='B':
                                print('down')
                        if key=='C':
                                print('right')
                        if key=='D':
                                print('left')

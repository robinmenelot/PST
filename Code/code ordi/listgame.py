from random import randint

def randomInt(mini, maxi):
        w = randint(mini,maxi)
        return w

play = True
x = randomInt(0,100)
y = int(input("Devine un chiffre entre 0 et 100:"))
print (x)

while play ==  True:

	if y>x:
		y = int(input("Moins:"))

	if y<x:
		y = int(input("Trop:"))
	
	if y==x:
		print("Yay !")
		play = False
print("Fin")
 


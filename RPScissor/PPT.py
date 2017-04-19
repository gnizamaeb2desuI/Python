import sys
import random

def Inici():
	print "####################################################"
	print "############# JOC PEDRA PAPER I TISORA #############"
	print "####################################################"

def Tria():
	print " "
	print " "
	print "Polsa la combinacio PE per la PEDRA"
	print "Polsa la combinacio PA pel PAPER"
	print "Polsa la combinacio TI per la TISORA"
	print "Polsa la combinacio SO per SORTIR"
	opcio = raw_input("Quina vols escollir?")
	if opcio == "PE":
		return "pedra"
	if opcio == "PA":
		return "paper"
	if opcio == "TI":
		return "tisora"
	if opcio == "SO":
		sys.exit(0)
	else:
		Tria()
	print " "
	print " "

def RandomTria():
	opcions = ["pedra", "paper", "tisora"]
	randomop = random.randint(0,2)
	return opcions[randomop]

def comparacio(nostra,random):
	if nostra == random:
		return "Empat"
	if nostra == "pedra" and random == "tisora":
		return "Guanya Jugador"
	if nostra == "paper" and random == "pedra":
		return "Guanya Jugador"
	if nostra == "tisora" and random == "paper":
		return "Guanya Jugador"
	else: 
		return "Guanya Ordinador"

if __name__=='__main__':
    Inici()
    nostra = Tria()
    random = RandomTria()
    resultat = comparacio(nostra, random)
    print "El resultat es: %s" % resultat


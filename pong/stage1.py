import pygame, sys
from pygame.locals import *

# Nombre de frames per segon
# Hem de canviar aquest valor per accelerar o disminuir
# la velocitat del joc

FPS = 200

# Usem aquestes variables gloabals per a definir
# la pantalla del nostre joc
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

def main():
	pygame.init()
	global DISPLAYSURF
	

	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption('Pong')
	
	while True: #el bucle del joc
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.exit()
				sys.exit()
	
	pygame.display.update()
	FPSCLOCK.tick(FPS)

if __name__ =='__main__':
	main()

import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH = 800
HEIGHT = 600
CELLSIZE = 10
assert WIDTH % CELLSIZE == 0,
assert HEIGHT % CELLSIZE == 0,
CELLWIDTH = WIDTH / CELLSIZE
CELLHEIGHT = HEIGHT / CELLSIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGRAY = (40, 40, 40)

def drawGrid():
	

def quit():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		#drawGrid
		pygame.display.update()

def main():
	pygame.init()
	global SCREENSURF
	SCREENSURF = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Game of Life")
	SCREENSURF.fill(WHITE)
	#drawGrid()
	pygame.display.update()

	quit()

if __name__ == '__main__':
	main()
import pygame, random, sys
from object import *
from display import *

# Running the physics engine

running = True
while running:
	screen.fill(BG)
	for object_ in particle_obj_list:
		object_.move()
		object_.bounce()
		object_.display()
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			(mouseX, mouseY) = pygame.mouse.get_pos()
			selected_particle = findParticle(my_particles, m)
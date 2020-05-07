import pygame
from display import *

BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
	def __init__(self, colour, WIDTH, HEIGHT):
		super().__init__()
		self.image = pygame.Surface([WIDTH, HEIGHT])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
		pygame.draw.rect(self.image, colour, 
						[0, 0, WIDTH,HEIGHT])
		self.rect = self.image.get_rect()

	def moveUp(self, pixels):
		self.rect.y -= pixels
		if self.rect.y < 0:
			self.rect.y = 0

	def moveDown(self, pixels):
		self.rect.y += pixels
		if self.rect.y > 400:
			self.rect.y = 400
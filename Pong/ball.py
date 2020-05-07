import pygame, random

BLACK = (0, 0, 0)

class Ball(pygame.sprite.Sprite):
	def __init__(self, colour, WIDTH, HEIGHT):
		super().__init__()
		self.image = pygame.Surface([WIDTH, HEIGHT])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
		pygame.draw.rect(self.image, colour, 
						[0, 0, WIDTH, HEIGHT])
		self.velocity = [random.randint(4,8),
						random.randint(-8,8)]
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]

	def bounce(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = random.randint(-8,8)

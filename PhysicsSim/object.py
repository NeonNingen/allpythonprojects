import pygame, random, math
from display import *
from gravity import *
BLUE = (0,0,255)

'''
Particle Class: Creates the object
move(self): The angle and speed at which particles move
			on the x and y axis
display(self): Drawing the object onto the screen
bounce(self): Makes the object stop colliding with the wall
'''
class Particle:

	def __init__(self, x,y, size):
		self.x = x
		self.y = y
		self.size = size
		self.colour = BLUE
		self.thickness = 1
		self.speed = 0.01
		self.angle = math.pi / 2

	def move(self):
		self.x += math.sin(self.angle) * self.speed 
		self.y -= math.cos(self.angle) * self.speed
		self.angle, self.speed = addVectors(
			self.angle, self.speed, gravity, 0.002)
		self.speed *= drag

	def display(self):
		pygame.draw.circle(
			screen, self.colour,(int(self.x), int(self.y)),
			self.size, self.thickness
			)

	def bounce(self):
		if self.x > WIDTH - self.size:
			self.x = 2 * (WIDTH - self.size) - self.x
			self.angle = - self.angle
			self.speed *= elasticity

		elif self.x < self.size:
			self.x = 2 * self.size - self.x
			self.angle = - self.angle
			self.speed *= elasticity

		if self.y > HEIGHT - self.size:
			self.y = 2 * (HEIGHT - self.size) - self.y
			self.angle = math.pi - self.angle
			self.speed *= elasticity

		elif self.y < self.size:
			self.y = 2 * self.size - self.y
			self.angle = math.pi - self.angle
			self.speed *= elasticity

# Creates multiple particles & Speed/Angle Movement
num_of_objects = 10
particle_obj_list = []

for _ in range(num_of_objects):
	size = random.randint(10, 20)
	x = random.randint(size, WIDTH - size)
	y = random.randint(size, HEIGHT - size)

	object_ = Particle(x, y, size)
	object_.speed = random.random()
	object_.angle = random.uniform(0, math.pi * 2)

	particle_obj_list.append(object_)



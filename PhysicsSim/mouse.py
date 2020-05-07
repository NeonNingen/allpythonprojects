import pygame, math

# Check to see if mouse is in the boundary of the particle
def findParticle(particles, x, y):
	for p in particles:
		if math.hypot(p.x-x, p.y-y) <= p.size:
			return p
	return None
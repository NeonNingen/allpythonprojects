import pygame, math

gravity = math.pi 
drag = 0.999
elasticity = 0.75


def addVectors(angle1, length1, angle2, length2):
	x = math.sin(angle1) * length1 + math.sin(angle2) * length2
	y = math.cos(angle1) * length1 + math.cos(angle2) * length2
	length = math.hypot(x, y)
	angle  = 0.5 * math.pi - math.atan2(y, x)
	return (angle, length)
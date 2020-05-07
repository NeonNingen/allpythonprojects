import arcade, random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Space Shooter"
SCALING = 2.0

class SpaceShooter(arcade.Window):
	def __init__(self, width, height, title):
		super().__init__(width, height, title)
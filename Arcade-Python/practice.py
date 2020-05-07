import arcade

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Welcome to Arcade"
RADIUS = 150

class Welcome(arcade.Window):
	def __init__(self):
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
		arcade.set_background_color(arcade.color.WHITE)

	def on_draw(self):
		arcade.start_render()

		arcade.draw_circle_filled(
			SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE
			)

if __name__ == "__main__":
	app = Welcome()
	arcade.run()
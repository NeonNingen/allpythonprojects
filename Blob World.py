import pygame
import random
from blob import Blob

STARTING_BLUE_BLOBS = 30
STARTING_RED_BLOBS = 9

WIDTH = 1280
HEIGHT = 720
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class BlueBlob(Blob):
    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary)
        self.color = BLUE


class RedBlob(Blob):
    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary)
        self.color = RED

    def move_fast(self):
        self.x += random.randrange(-7, 7)
        self.y += random.randrange(-7, 7)


def draw_env(blob_list):
    game_display.fill(BLACK)

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.check_bounds()

    pygame.display.update()


# noinspection PyTypeChecker
def main():
    blue_blobs = dict(enumerate([BlueBlob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    print(blue_blobs)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_env([blue_blobs, red_blobs])
        clock.tick(60)
        # print(blue_blob.x, blue_blob.y)


if __name__ == "__main__":
    main()

import pygame, sys

def main():
    pygame.init()
    DISPLAY = pygame.display.set_mode((1000,500),0,32)
    WHITE = (255,255,255)
    blue = (0,0,255)
    DISPLAY.fill(WHITE)
    pygame.mouse.set_visible(False)
    pygame.draw.rect(DISPLAY, blue,(480,200,50,250))
    pygame.display.update()
    pygame.mouse.set_pos(480, 200)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                pos = event.pos
                pygame.draw.rect(DISPLAY, blue, (pos[0]-25,pos[1], 50, 250))
                pygame.display.update()
                DISPLAY.fill(WHITE)

        for event in pygame.event.get(pygame.KEYUP):
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
                sys.exit()
main()
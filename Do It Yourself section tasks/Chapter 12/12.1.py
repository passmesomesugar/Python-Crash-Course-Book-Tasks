import sys
import pygame


class BlueBackground:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.bg_color = (0, 0, 255)
        self.screen.fill(self.bg_color)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    blue_sky = BlueBackground()
    blue_sky.run_game()

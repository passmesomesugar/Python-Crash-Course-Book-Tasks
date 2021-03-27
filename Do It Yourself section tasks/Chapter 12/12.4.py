# 12-4. Keys: Make a Pygame file that creates an empty screen. In the event
# loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected.
# Run the program and press various keys to see how Pygame responds.

import pygame
import sys


class EmptyBackground:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))

    def run_game(self):
        while True:
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event.key)


if __name__ == '__main__':
    empty_bg = EmptyBackground()
    empty_bg.run_game()

# 12-2. Game Character: Find a bitmap image of a game character you like or
# convert an image to a bitmap. Make a class that draws the character at the
# center of the screen and match the background color of the image to the background
# color of the screen, or vice versa.
import sys
import pygame

from settings_for_character import Settings
from vivi import Vivi


class Character:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Vivi")
        self.vivi = Vivi(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.vivi.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    vv = Character()
    vv.run_game()

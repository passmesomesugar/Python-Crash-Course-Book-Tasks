import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf


class AlienInvasion:

    def run_game():
        pygame.init()
        ai_settings = Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption("Alien invasion")
        ship = Ship(ai_settings, screen)
        bullets = Group()

        while True:
            gf.check_events(ai_settings, screen, ship, bullets)
            ship.update()
            bullets.update()
            gf.update_screen(ai_settings, screen, ship, bullets)
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()
            # screen.fill(ai_settings.bg_color)
            # ship.blitme()
            # pygame.display.flip()

    run_game()


#     self.settings = Settings()
#     self.screen = pygame.display.set_mode((0, 0))
#     self.settings.screen_width = self.screen.get_rect().width
#     self.settings.screen_height = self.screen.get_rect().height
#     pygame.display.set_caption("Alien invasion")
#     # ship = Ship(ai_settings, screen)
#     self.ship = Ship(self)
#
# def run_game(self):
#     while True:
#         self._check_events()
#         self.ship.update()
#         self._update_screen()
#
# def _check_events(self):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             self._check_keydown_events(event);
#         elif event.type == pygame.KEYUP:
#             self._check_keyup_events(event);
#
# def _check_keydown_events(self, event):
#     if event.key == pygame.K_RIGHT:
#         self.ship.moving_right = True
#     elif event.key == pygame.K_LEFT:
#         self.ship.moving_left = True
#     elif event.key == pygame.K_q:
#         sys.exit()
#
# def _check_keyup_events(self, event):
#     if event.key == pygame.K_RIGHT:
#         self.ship.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         self.ship.moving_left = False
#
# def _update_screen(self):
#     self.screen.fill(self.settings.bg_color)
#     self.ship.blitme()
#
#     pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

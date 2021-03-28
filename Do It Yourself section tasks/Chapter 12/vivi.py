import pygame


class Vivi:

    def __init__(self, vivi_display):
        self.screen = vivi_display.screen
        self.screen_rect = vivi_display.screen.get_rect()

        self.image = pygame.image.load('images/vivi.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

import pygame


class Rocket:

    def __init__(self, rg_game):
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.screen_rect = rg_game.screen.get_rect()

        self.image = pygame.image.load('images/rocket.png')
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left:
            self.rect.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top:
            self.rect.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.rocket_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

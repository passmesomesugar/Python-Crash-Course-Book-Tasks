import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.ai_settings = ai_settings
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        """Draw the shit at its current location."""
        self.screen.blit(self.image, self.rect)
    #     self.settings = ai_game.settings
    #     self.screen_rect = ai_game.screen.get_rect()
    #
    #     self.center = float(self.screen_rect.centerx)
    #     self.image = pygame.image.load('images/ship.bmp')
    #     self.image = pygame.transform.scale(self.image, (100, 150))
    #     self.rect = self.image.get_rect()
    #
    #     self.rect.midbottom = self.screen_rect.midbottom
    #
    #     self.x = float(self.rect.x)
    #
    #     self.moving_right = False
    #     self.moving_left = False
    #
    # def update(self):
    #     if self.moving_right:
    #         self.rect.x += self.settings.ship_speed_factor
    #     if self.moving_left:
    #         self.rect.x -= self.settings.ship_speed_factor
    #     self.rect.centerx = self.center
    #
    # def blitme(self):
    #     self.screen.blit(self.image, self.rect)

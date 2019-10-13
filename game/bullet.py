import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ class for manage bullets """

    def __init__(self, ai_settings, screen, ship):
        """ create bullet object in current position if ship """
        super().__init__()
        self.screen = screen

        # create bullet in (0,0) position and add correct position
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # bullet position in float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ bullet moving up """

        # update bullet position in float
        self.y -= self.speed_factor

        # update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ draw bullet at screen """
        pygame.draw.rect(self.screen, self.color, self.rect)

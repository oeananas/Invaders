import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ alien class """

    def __init__(self, ai_settings, screen):
        """ init alien in previous position """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image and set rect attr
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # every alien in left-top part of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save the alien position
        self.x = float(self.rect.x)


    def blitme(self):
        """ print alien """
        self.screen.blit(self.image, self.rect)

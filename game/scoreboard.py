import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    """ game info class """
    def __init__(self, ai_settings, screen, stats):
        """ init score attr """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # score font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # prepare images score
        self.prep_score()
        self.prep_hight_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """ transform score to image """
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.ai_settings.bg_color)

        # score output on right top part of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_hight_score(self):
        """ record score on screen """
        hight_score = int(round(self.stats.hight_score, -1))
        hight_score_str = "{:,}".format(hight_score)
        self.hight_score_image = self.font.render(
            hight_score_str, True, self.text_color, self.ai_settings.bg_color)

        # record on top center of screen
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.score_rect.top

    def show_score(self):
        """ display score """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # display ships
        self.ships.draw(self.screen)

    def prep_level(self):
        """ transform level to image """
        self.level_image = self.font.render(
            str(self.stats.level),
            True, self.text_color, self.ai_settings.bg_color)

        # display level under score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.top + 30

    def prep_ships(self):
        """ num of availible ships """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

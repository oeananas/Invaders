class GameStats():
    """ statistic """

    def __init__(self, ai_settings):
        """ init statistic """
        self.ai_settings = ai_settings
        # run game in no acnive
        self.game_active = False
        self.reset_stats()

        # record score not reset
        self.hight_score = 0

    def reset_stats(self):
        """ init statistic in current game """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

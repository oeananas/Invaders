class GameStats():
    """ statistic """

    def __init__(self, ai_settings):
        """ init statistic """
        self.ai_settings = ai_settings
        # run game in no acnive
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """ init statistic in current game """
        self.ships_left = self.ai_settings.ship_limit

class GameStats():
    """ statistic """

    def __init__(self, ai_settings):
        """ init statistic """
        self.ai_settings = ai_settings
        # active run game
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """ init statistic in current game """
        self.ships_left = self.ai_settings.ship_limit

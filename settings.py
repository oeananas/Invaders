class Settings():
    """ main game settings class """

    def __init__(self):
        """ init static game settings """
        # screen params
        self.screen_width = 900
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # ship params
        self.ship_limit = 3

        # bullet params
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # aliens params
        self.fleet_drop_speed = 20

        # game speed
        self.speedup_scale = 1.1
        # score scale
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ init dynamic settings """
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 15
        self.alien_speed_factor = 1
        # fleet_direction = 1 move right, -1 move left
        self.fleet_direction = 1
        # score
        self.alien_points = 50

    def increase_speed(self):
        """ increase game speed and score scale"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

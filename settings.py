class Settings():
    """ main game settings class """

    def __init__(self):
        """ init game settings """
        # screen params
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship params
        self.ship_speed_factor = 5

        # bullet params
        self.bullet_speed_factor = 15
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

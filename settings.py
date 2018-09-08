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
        self.ship_limit = 3

        # bullet params
        self.bullet_speed_factor = 15
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # aliens params
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        # fleet_direction = 1 move right, -1 move left
        self.fleet_direction = 1

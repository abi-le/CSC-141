
class Settings:
    '''a class to start all settings for Squirtle Go'''

    def __init__(self):
        '''initialize game settings'''
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

    # squirtle's speed
        self.squirtle_speed = 1.5

    # bullet setings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100000
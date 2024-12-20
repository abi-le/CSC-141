
class Settings:
    '''a class to start all settings for Squirtle Go'''

    def __init__(self):
        '''initialize game settings'''
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

    # squirtle's speed
        self.squirtle_speed = 4.5
        self.squirtle_limit = 3 

    # bullet setings
        self.bullet_speed = 12.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10000000

    # alien settings 
        self.charizard_speed = 6.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right, -1 represnts left
        self.fleet_direction = 1

    #how quickly the game speeds up
        self.speedup_scale = 1.1
        #how quickly the charizard point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''initialize settings that change throughout the game'''
        self.squirtle_speed = 4.5
        self.bullet_speed = 12.0
        self.charizard_speed = 6.0

        #fleet direction of 1 respresents right; -1 represents left.
        self.fleet_direction = 1

        # scoring settings
        self.charizard_points = 50

    def increase_speed(self):
        '''increase speed settings and charizard point values'''
        self.squirtle_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.charizard_speed *= self.speedup_scale

        self.charizard_points = int(self.charizard_points * self.score_scale)
        

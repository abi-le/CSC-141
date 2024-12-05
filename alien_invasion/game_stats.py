

class GameStats:
    '''track stats for squirtle go'''

    def __init__(self, sg_game):
        '''initialize stats'''
        self.settings = sg_game.settings
        self.reset_stats()

    def reset_stats(self):
        '''initialize stats that can change during the game'''
        self.squirtles_left = self.settings.squirtle_limit
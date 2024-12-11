import pygame.font
from pygame.sprite import Group

from squirtle import Squirtle

class Scoreboard:
    '''a class to report scoring information'''

    def __init__(self, sg_game):
        '''initialize scorekeeping attributes'''
        self.sg_game = sg_game
        self.screen = sg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sg_game.settings
        self.stats = sg_game.stats

        #font settings for storing information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_squirtles
    
    def prep_score(self):
        '''turn rhe score into a rendered image'''
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''draw the scores, level, and squirtles to the screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #Sself.squirtles.draw(self.screen)

    def prep_high_score(self):
        '''turn the high score into a a rendered image'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        '''check to see if there's a new high score'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    
        
    def prep_level(self):
        '''turn the level into a rendered image'''
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        #position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_squirtles(self):
        '''show how many ships are left'''
        self.squirtles = Group()
        for squirtle_number in range(self.stats.squirtles_left):
            squirtle = Squirtle(self.sg_game)
            squirtle.rect.x = 10 + squirtle_number * squirtle.rect.width
            squirtle.rect.y = 10
            self.squirtles.add(squirtle)
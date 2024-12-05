import pygame
from pygame.sprite import Sprite 
from settings import Settings

class Charizard(Sprite):
    '''A class to represent a single alien in the fleet'''

    def __init__(self, sg_game):
        '''initialize the alien and set its starting position'''
        super().__init__()
        self.screen = sg_game.screen
        self.settings = sg_game.settings
        self.screen_rect = sg_game.screen.get_rect()

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('charizard.png')
        self.image = pygame.transform.scale(self.image, (180, 170))
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #start each at top of the screen.
        self.rect.top = self.screen_rect.top

        #store the aliens exact horizontal position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        '''return True if charizard is at edge of screen'''
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        '''move charizard to the right'''
        self.x += self.settings.charizard_speed * self.settings.fleet_direction
        self.rect.x = self.x
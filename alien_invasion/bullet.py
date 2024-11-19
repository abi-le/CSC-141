
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''a class to manage water fired from squirtle'''

    def __init__(self, sg_game):
        '''create an object at squirtle's current position'''
        super().__init__()
        self.screen = sg_game.screen
        self.settings = sg_game.settings
        self.color = self.settings.bullet_color

        #create a water bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                self.settings.bullet_height)
        self.rect.midtop = sg_game.squirtle.rect.midtop

        #store water bullet's position as a float
        self.y = float(self.rect.y)

    def update(self):
        '''move the water bullet up the screen'''
        #update exact position of the bullet
        self.y -= self.settings.bullet_speed
        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        '''draw the bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)

import pygame  # type: ignore

from settings import Settings
class Squirtle:
    '''a class to manage squirtle'''

    def __init__(self, sg_game):
        '''initialize squirtle and his starting position'''
        self.screen = sg_game.screen
        self.settings = sg_game.settings
        self.screen_rect = sg_game.screen.get_rect()

        #load squirtle image and get its rect
        self.image = pygame.image.load('squirtle_character.bmp')
        self.image = self.image.convert()
        self.image.set_colorkey(self.image.get_at((1,1)))


        self.rect = self.image.get_rect()

        #start each squirtle are the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        #movement flag; start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        '''update squirtles position based on the movement flag'''
        #update squirtles x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.squirtle_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.squirtle_speed

        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        '''draw squirtle at his current location'''
        self.screen.blit(self.image, self.rect)
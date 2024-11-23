'''Plan: In my game, the player will control squirtle at the bottom of the 
screen. The character can move left and right and shoot water balls at the
enimies raining down on them. The enemies move across and down the screen.
The player shoots to destory the enemies and once the enemies are destoyed,
more enemies appear and are faster than the last group of enemies. If an 
enemy reaches squirtle, you have three lives to use before the game will end.'''

import sys 
import pygame  # type: ignore

from settings import Settings 
from squirtle import Squirtle
from bullet import Bullet 

#initialize pyagme
pygame.init()

#set screen
screen = pygame.display.set_mode((1800, 860))
# #load background imange
background = pygame.image.load('background.jpg')
#scale background image to fit the screen
background = pygame.transform.scale(background, (1800, 860))


class SquirtleGo:
    '''class to manage game assets and behavior'''

    def __init__(self):
        '''initialize the game, and create game resources'''
        pygame.init()

        # controlling frame rate
        self.clock = pygame.time.Clock()   
        self.settings = Settings()

        #run the game full screen
        
        self.screen = pygame.display.set_mode((1800, 800), pygame.FULLSCREEN)

        #create a display window
        
        pygame.display.set_caption("Squirtle Go!")

        #create ship
        self.squirtle = Squirtle(self)
        #create bullets
        self.bullets = pygame.sprite.Group()
    
    #manages screen updates
    def run_game(self):
        '''start the main loop for the game'''
        while True:
            #draw the background image on the screen
            screen.blit(background, (0,0))
            # self._check_events()
            self.squirtle.update()
            self._update_bullets()  
            # self._update_screen()
            # controlling frame rate
            self.clock.tick(60)
            
            # watch for keyboard and mouse events
            # event is an action the user performs 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.K_ESCAPE:
                    sys.exit()

            
            
            #redraw the screen during each pass through the loop
            '''QUESTION'''
            # self.screen.fill(background)
            self.squirtle.blitme()

            #update display
            pygame.display.update()

            #make the most recently drawn screen visible
            pygame.display.flip()
            # self.clock.tick(60)
            
            #the loop runs exactly 60 times per second
    def _update_bullets(self):
        '''update position of bullets and get rid of old bullets'''
        #update bullet positions
        self.bullets.update()
        #get rid of bullets that have disappeared       
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        
    def _update_screen(self):
        '''update images on the screen, and flip to the new screen'''
             
        self.squirtle.blitme()


        pygame.display.flip()

    #check whether the player has clicked to close the window
    def _check_events(self):
        '''respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                sys.exit()

            #Movement
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.squirtle.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.squirtle.moving_left = True
            #pressing Q to quit
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        '''respond to key releases'''
        if event.key == pygame.K_RIGHT:
            self.squirtle.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.squirtle.moving_left = False

    def _fire_bullet(self):
        '''create a new bullet and add it to the bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
               

if __name__ == '__main__':
    #make an instance, and run the game.
    sg = SquirtleGo()
    sg.run_game() 
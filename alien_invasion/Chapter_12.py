'''Plan: In my game, the player will control squirtle at the bottom of the 
screen. The character can move left and right and shoot water balls at the
enimies raining down on them. The enemies move across and down the screen.
The player shoots to destory the enemies and once the enemies are destoyed,
more enemies appear and are faster than the last group of enemies. If an 
enemy reaches squirtle, you have three lives to use before the game will end.'''

import sys 
from time import sleep

import pygame  # type: ignore

from settings import Settings 
from game_stats import GameStats
from button import Button
from squirtle import Squirtle
from bullet import Bullet 
from charizard import Charizard

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

        #create an instance to store game stats
        self.stats = GameStats(self)

        #create ship
        self.squirtle = Squirtle(self)
        #create bullets
        self.bullets = pygame.sprite.Group()

        self.charizards = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = True

        #start squirtle go in an inactive state
        self.game_active = False

        #make a play button
        self.play_button = Button(self, "Play")
    
    #manages screen updates
    def run_game(self):
        '''start the main loop for the game'''
        while True:
            #draw the background image on the screen
            screen.blit(background, (0,0))
            # self._check_events()

            if self.game_active:
                self.squirtle.update()
                self._update_bullets()  
                self._update_charizards()
            
            self._update_screen()
            #controlling frame rate
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

        self._check_bullet_charizard_collisions()
  

    def _check_bullet_charizard_collisions(self):
        #check for any bullets that have hit charizards
        #get rid of the bullet and the charizard
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.charizards, True, True)
        
        if not self.charizards:
        #destory existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet
            self.settings.increase_speed()
        
    def _update_screen(self):
        '''update images on the screen, and flip to the new screen'''
             
        self.squirtle.blitme()
        self.charizards.draw(self.screen)

        #draw play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    #check whether the player has clicked to close the window
    def _check_events(self):
        '''respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            #Movement
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        '''start a new game when the player clicks Play'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #reset the game settings
            self.settings.initialize_dynamic_settings()
            #reset the game statistics
            self.stats.reset_stats()
            self.game_active = True
            print ("Hello!")

            #get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.charizards.empty()

            #create new fleet and center the ship
            self._create_fleet()
            self.squirtle.center_ship()

            #hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        '''respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.squirtle.moving_right = True
            self.squirtle.facing_left = False
        elif event.key == pygame.K_LEFT:
            self.squirtle.moving_left = True
            self.squirtle.facing_left = True
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

    def _create_fleet(self):
        '''create fleet of charizards'''
        #make charizard and keep adding charzards until there's no room left
        #spacing between charizards is one charizard
        charizard = Charizard(self)
        charizard_width, charizard_height = charizard.rect.size

        current_x, current_y = charizard_width, charizard_height

        while current_y < (self.settings.screen_height - 2 * charizard_height):
            while current_x < (self.settings.screen_width - 1 * charizard_width):
                self._create_charizard(current_x, current_y)
                current_x += 2 * charizard_width 
            
            #finished a row, reset x value, and increment y value
            current_x = charizard_width
            current_y += 1 * charizard_height

    def _create_charizard (self, x_position, y_position):
        '''create a charizard and place it in the row'''
        new_charizard = Charizard(self)
        new_charizard.x = x_position
        new_charizard.rect.x = x_position
        new_charizard.rect.y = y_position
        self.charizards.add(new_charizard)

    def _check_fleet_edges (self):
        '''respond appropriatelt if any aliens have reached an edge'''
        for charizard in self.charizards.sprites():
            if charizard.check_edges():
                self._change_fleet_direction()
                break

    
    def _change_fleet_direction(self):
        '''drop the entire fleet and change the fleet's direction'''
        for charizard in self.charizards.sprites():
            charizard.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_charizards(self):
        '''update the positions of all the charizards in the fleet'''
        self._check_fleet_edges()
        self.charizards.update()

        #look for charizard-ship collisions
        if pygame.sprite.spritecollideany(self.squirtle, self.charizards):
            self._ship_hit()
            print ("Squirtle hit!")

        #look for charizards hitting the bottom of the screen
        self._check_charizards_bottom()

    def _ship_hit(self):
        '''respond to the squirtle being hit by an charizard'''
        #decrement squirtles left
        if self.stats.squirtles_left > 0:
            self.stats.squirtles_left -= 1

            #get rid of any remaining bullets and charizards
            self.bullets.empty()
            self.charizards.empty()

            #create new fleet and enter squirtle
            self._create_fleet()
            self.squirtle.center_squirtle()

            #pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_charizards_bottom(self):
        '''check if any charizards have reached the bottom of the screen'''
        for charizards in self.charizards.sprites():
            if charizards.rect.bottom >= self.settings.screen_height:
            #treat this the same as if squirtle got hiy
                self._ship_hit()
                break
               

if __name__ == '__main__':
    #make an instance, and run the game.
    sg = SquirtleGo()
    sg.run_game() 
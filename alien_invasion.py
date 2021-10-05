# represents the game itself

import sys
import pygame
# Step 3, creating settings.py and importing initial screen settings
from settings import Settings
# Step 4, creating ship.py and importing in class to use
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()  # Initializes pygame background settings needed
        self.settings = Settings()

        # Actual object assigned to self.screen is called a "surface". It is a visible layer that can contain game
        # elements. Each element in the game, like a ship or an alien, is its own surface.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # this surface represents entire game window/frame, originally (1200,800) was passed into set_mode for testing
        # but refactored after settings.py created

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # the self being passed is the instance of the game which is the one arg needed
        self.bullets = pygame.sprite.Group()  # Group behaves like a list, will store all live bullets
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Step 2 Set background color
        # self.bg_color = (230, 230, 230) Step 3, no longer needed once settings.py created

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()  # Step 4 Refactor - create helper method
            self.ship.update()  # Step 5 Ship movement flag check
            self._update_bullets()
            self._update_aliens()

            print(len(self.bullets))
            self._update_screen()  # Step 4 Refactor - create helper method

    def _check_events(self):
        """Event loop that watches for keyboard and mouse events"""
        # pygame.event.get() returns list of detected events that have occurred since loop last run
        # Any event will cause this loop to run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Step 5 Check for keydown event
                self._check_keydown_events(event)  # Step 6 - use helper method
            elif event.type == pygame.KEYUP:  # Step 5 Check for keyup event
                self._check_keyup_events(event)  # Step 6 - use helper method

    def _check_keydown_events(self, event):  # Step 6 Refactored check_events
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:  # Is keydown the right arrow
            # Move the ship to the right
            # self.ship.rect.x += 1  Used for initial testing of Step 5, now adding continuous movement via
            # the ship instance
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # Is keydown the left arrow
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):  # Step 6 Refactored check_events
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:  # Is keyup the right arrow
            # stop right movement
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:  # limits number of live bullets
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)  # add is like append but written for pygame games

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets have have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        """Update the positions of aliens in the fleet"""
        self.aliens.update()  # calls update on every alien in group

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Step 2 Redraw the screen during each pass through the loop
        # fill() is a surface method, originally self.bg_color for testing, refactored to settings property
        self.screen.fill(self.settings.bg_color)
        # draw ship in its current position which places it on top of the background surface
        self.ship.blitme()
        for bullet in self.bullets.sprites():  # goes through list of all sprites in bullets and draw each one
            bullet.draw_bullet()
        # draws each element in the group at the position defined by rect, only required argument for draw() is a
        # surface on which to draw the group elements
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Make an alien and find the number of aliens in a row
        # Side margins are 1 alien width, space between each alien is equal to one alien width
        alien = Alien(self)  # ai_game automatically passed in with self
        alien_width, alien_height = alien.rect.size   # size contains a tuple with width and height of a rect
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row
            # alien = Alien(self) refactored out
            # alien.x = alien_width + (2 * alien_width) * alien_number  refactored out
            # alien.rect.x = alien.x   refactored out
            # self.aliens.add(alien)   refactored out
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width) * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + (2 * alien_height) * row_number
        self.aliens.add(alien)

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
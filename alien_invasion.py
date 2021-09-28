# represents the game itself

import sys
import pygame
# Step 3, creating settings.py and importing initial screen settings
from settings import Settings
# Step 4, creating ship.py and importing in class to use
from ship import Ship


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

        # Step 2 Set background color
        # self.bg_color = (230, 230, 230) Step 3, no longer needed once settings.py created

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()  # Step 4 Refactor - create helper method
            self._update_screen()  # Step 4 Refactor - create helper method



    def _check_events(self):
        """Event loop that watches for keyboard and mouse events"""
        # pygame.event.get() returns list of detected events that have occurred since loop last run
        # Any event will cause this loop to run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Step 2 Redraw the screen during each pass through the loop
        # fill() is a surface method, originally self.bg_color for testing, refactored to settings property
        self.screen.fill(self.settings.bg_color)
        # draw ship in its current position which places it on top of the background surface
        self.ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
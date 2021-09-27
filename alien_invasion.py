# represents the game itself

import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()  # Initializes pygame background settings needed

        # Actual object assigned to self.screen is called a "surface". It is a visible layer that can contain game
        # elements. Each element in the game, like a ship or an alien, is its own surface.
        self.screen = pygame.display.set_mode((1200, 800))  # this surface represents entire game window/frame
        pygame.display.set_caption("Alien Invasion")

        # Step 2 Set background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Event loop that watches for keyboard and mouse events
            # pygame.event.get() returns list of detected events that have occurred since loop last run
            # Any event will cause this loop to run
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Step 2 Redraw the screen during each pass through the loop
            #  - background color
            self.screen.fill(self.bg_color)  # fill() is a surface method

            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
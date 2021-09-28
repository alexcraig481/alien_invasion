import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):  # instance of game will be passed to ship
        """Initialize the ship and set its starting position"""

        # Pygame lets you treat all game elements like rectangles, which is efficient when determining location of
        # elements in relation to one another
        self.screen = ai_game.screen  # allows us to access game screen easily in ship methods
        self.screen_rect = ai_game.screen.get_rect()   # This allows us to place in the ship in the correct location
        # on the screen

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()  # this attribute will be used later to place ship

        # Start each new ship at the bottom center of the screen
        # Using the the midbottom point of screen's rect to establish origin midpoint of ship's rect
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag, Step 5, Adding for continuous movement
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draws the ship at its current location"""
        self.screen.blit(self.image, self.rect)

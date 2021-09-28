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
        self.settings = ai_game.settings  # Step 5 Adding ship speed to settings

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()  # this attribute will be used later to place ship

        # Start each new ship at the bottom center of the screen
        # Using the the midbottom point of screen's rect to establish origin midpoint of ship's rect
        self.rect.midbottom = self.screen_rect.midbottom
        # Step 5 Store a decimal value for the ship's horizontal position so we can add float movement to it
        self.x = float(self.rect.x)

        # Movement flag, Step 5, Adding for continuous movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        # Changed so the ship's x value is updated, not the rect, this way we can keep track of float speed,
        # rect only does int
        if self.moving_right and self.rect.right < self.screen_rect.right:  # compare position to screen boundaries
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:  # compare position to screen boundaries
            self.x -= self.settings.ship_speed

        # Update rect obj from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draws the ship at its current location"""
        self.screen.blit(self.image, self.rect)

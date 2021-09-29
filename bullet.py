import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # inheriting from Sprite - allows grouping of related elements and act on all of them at once
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Rect() draws a bullet according to width & height using 0,0 as top left of bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop  # Make bullet appear to be coming up ship

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to screen"""
        pygame.draw.rect(self.screen, self.color.self.rect)
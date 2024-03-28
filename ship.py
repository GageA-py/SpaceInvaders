import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, si_game):
        """Initialize ship and starting position."""
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.screen_rect = si_game.screen.get_rect()

        # Load ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value of the ship position
        self.x = float(self.rect.x)

        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update ship position based on movement flags"""
        # Update ship's x value not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Center ship at the bottom of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        

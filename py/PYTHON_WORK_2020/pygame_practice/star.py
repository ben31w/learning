import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A realistic star sprite."""
    # star_scene is an instance of StarScene
    def __init__(self, star_scene):
        """Initialize the star."""
        super().__init__()
        self.screen = star_scene.screen

        # Image of the star and its rect.
        self.image = pygame.image.load('images/realistic_star_simple.bmp')
        self.rect = self.image.get_rect()

        # Store the star's coordinates as exact decimals.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
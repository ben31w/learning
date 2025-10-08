import sys

import pygame

class Game:
    """A game featuring a blue background and Super Mario!"""

    def __init__(self):
        """Initialize attributes."""
        pygame.init()
        
        # The screen
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Super Mario")

        # Light blue background color
        self.bg_color = (153, 217, 234)

        # Mario image
        self.mario = pygame.image.load('images/mario_blue_background.bmp')

    def run_game(self):
        """Starts the main loop for the game."""
        while True:
            # Event loop watches for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen and Mario during each pass through the while loop.
            self.screen.fill(self.bg_color)
            self.screen.blit(self.mario , self.mario.get_rect())

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run_game()
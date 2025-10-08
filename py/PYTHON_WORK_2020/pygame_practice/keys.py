import sys
import pygame

class KeypressGame:
    """
    In this 'game', every time you press a key, the corresponding event.key 
    attribute will be printed.
    """

    def __init__(self):
        """Initialize pygame attributes."""
        pygame.init()

        self.screen = pygame.display.set_mode((300, 1))
        pygame.display.set_caption("Press a key.")

    def _check_events(self):
        """Check for key events and print key attributes."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))

    def run_game(self):
        """Run the game."""
        while True:
            self._check_events()

if __name__ == '__main__':
    kg = KeypressGame()
    kg.run_game()
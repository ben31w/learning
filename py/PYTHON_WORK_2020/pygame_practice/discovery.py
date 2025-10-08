import sys

import pygame

class MoveTheSpaceShuttle:
    """A simple game where users control a space shuttle using arrow keys."""

    def __init__(self):
        """Initialize attributes."""
        pygame.init()
        
        # The screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Discovery")

        # The space shuttle and its rect
        self.discovery = pygame.image.load('images/discovery.bmp')
        self.discovery_rect = self.discovery.get_rect()

        # Put the space shuttle in the middle of the screen.
        self.discovery.get_rect().center = self.screen.get_rect().center

    def _check_events(self):
        """Check for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_RIGHT:
                    self.discovery.get_rect().x += 1
                if event.key == pygame.K_LEFT:
                    self.discovery.get_rect().x -= 1
                if event.key == pygame.K_UP:
                    self.discovery.get_rect().y += 1
                if event.key == pygame.K_DOWN:
                    self.discovery.get_rect().y -= 1


    def _update_screen(self):
        """Update the screen."""
        self.screen.fill((0 , 0, 0))
        self.screen.blit(self.discovery, self.discovery.get_rect())
        pygame.display.flip()

    def run_game(self):
        """Runs the game."""
        while True:
            self._check_events()
            self._update_screen()

if __name__ == '__main__':
    game = MoveTheSpaceShuttle()
    game.run_game()
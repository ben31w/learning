import sys
import pygame
from random import randint

from star import Star

class StarScene:
    """A window filled with stars."""

    def __init__(self):
        """Initialize attributes and set up screen."""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Starry Night")
        self.bg_color = (64, 64, 64)

    def check_events(self):
        """Checks for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()

    def draw_scene(self):
        """Draw the starry scene."""
        # Use a star to determine how many will fit in a row.
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen.get_rect().width - star_width/2
        stars_per_row = int(available_space_x // (1.5 * star_width))
        print(available_space_x)
        print(stars_per_row)

        # Determine how many rows will fit on screen.
        available_space_y = self.screen.get_rect().height - star_height/2
        number_of_rows = int(available_space_y // (1.5 * star_height))
        print(available_space_y)
        print(number_of_rows)

        # Create the grid of stars.
        for row_number in range(number_of_rows):
            for star_number in range(stars_per_row):
                random_value = randint(-40, 40)
                star = Star(self)
                star.x = star_width/2 + 1.5 * star_width * star_number + random_value
                star.y = star_height/2 + 1.5 * star_height * row_number + random_value
                star.rect.x = int(star.x)
                star.rect.y = int(star.y)
                self.screen.blit(star.image, star.rect)

    def run_game(self):
        """Runs the program."""
        self.screen.fill(self.bg_color)
        self.draw_scene()
        while True:
            self.check_events()
            pygame.display.flip()

if __name__ == '__main__':
    ss = StarScene()
    ss.run_game()
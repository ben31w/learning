import json

"""Contains a class and methods to manage Alien Invasion's statistics."""

class GameStats:
    """Track statistics for Alien Invasion."""

    # ai_game is an instance of the AlienInvasion class.
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False
        self.game_paused = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.high_score = get_high_score()


def get_high_score():
    """Load and return the high score stored in high_score.json."""
    filename = 'high_score.json'
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return 0

def set_high_score(num):
    """Set a new high score to be stored in high_score.json."""
    filename = 'high_score.json'
    with open(filename, 'w') as f:
        json.dump(num, f)
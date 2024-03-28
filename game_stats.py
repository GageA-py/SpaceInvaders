class GameStats:
    """Track stats for Space Invaders."""

    def __init__(self, si_game):
        """Initialize the statistics"""
        self.settings = si_game.settings
        self.reset_stats()

        # Start Space Invaders in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0
    
    def reset_stats(self):
        """Initialize the statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1 
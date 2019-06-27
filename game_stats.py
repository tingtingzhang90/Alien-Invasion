class GameStats():

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active = False
        # High score should never be reset.
        with open('high_score.txt') as file_object:
            contents = file_object.read()
        self.high_score = int(contents)

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
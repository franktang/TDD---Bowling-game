class Game:
    game_string = ""
    total_score = 0
    def __init__(self, game_string):
        self.game_string = game_string

    def get_score(self):
        for hit_score in self.game_string:
            if hit_score != '-':
                self.total_score += int(hit_score)

        return self.total_score
    
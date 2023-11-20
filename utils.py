class Helper:
    def __init__(self):
        self.rounds_to_update = []

    def compare_rounds(self, round1, round2):
        return round1.number == round2.number and self.compare_games(round1.games, round2.games)

    def compare_games(self, games1, games2):
        return all(
            game1.home_team == game2.home_team and
            game1.away_team == game2.away_team and
            game1.score == game2.score
            for game1, game2 in zip(games1, games2)
        )

    def find_different_rounds(self, old_rounds, new_rounds):
        different_rounds = []
        for old_round, new_round in zip(old_rounds, new_rounds):
            if not self.compare_rounds(old_round, new_round):
                different_rounds.append(new_round)
        return different_rounds

    
helper = Helper()
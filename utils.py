class Helper:
    def __init__(self):
        self.games_to_update = []

    def compare_rounds(self, db_round, scraped_round):
        return db_round.number == scraped_round.number and self.compare_games(db_round.games, scraped_round.games)

    def compare_games(self, db_games, scraped_games):
        are_equal = True
        for db_game, scraped_game in zip(db_games, scraped_games):
            if (
                db_game.home_team == scraped_game.home_team and
                db_game.away_team == scraped_game.away_team and
                db_game.score != scraped_game.score
            ):
                self.games_to_update.append(scraped_game)
                are_equal = False
        
        return are_equal
        
        
    def find_different_rounds(self, old_rounds, new_rounds):
        different_rounds = []
        for old_round, new_round in zip(old_rounds, new_rounds):
            if not self.compare_rounds(old_round, new_round):
                different_rounds.append(new_round)
                
        games_to_update = self.games_to_update
        self.games_to_update = []
        return different_rounds, games_to_update

    
helper = Helper()
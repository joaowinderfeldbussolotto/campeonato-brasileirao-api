from database.database import update_scores, update_table, update_round, get_rounds, update_rounds
from services.scraping.table_scraping import scrap_table
from services.scraping.rounds_scraping import scrap_rounds
from core.config import initiate_database
from datetime import datetime
from utils import helper
from services.email_service import send_email
from services.scraping.live_games_scraping import scrap_live_games

async def init_rounds():
    rounds = scrap_rounds()
    if len(rounds) == 0: return
    await update_rounds(rounds)


async def populate_table():
    tournamente_table = scrap_table()
    await update_table(tournamente_table)

async def populate_rounds():
    print('running update_rounds')
    rounds = scrap_rounds()
    if len(rounds) == 0:
        return
    rounds_db = await get_rounds().to_list()
    rounds_to_update = helper.find_different_rounds(rounds_db, rounds)
    for r in rounds_to_update:
        print('updating rounds')
        await update_round(r)

async def populate_database():
    print(datetime.now())
    await initiate_database()
    await populate_table()
    await populate_games()

async def populate_games():
    games_changed = []
    live_games = scrap_live_games()
    for live_game in live_games:
        live_game = live_game.__dict__
        game = await update_scores(live_game['home_team'], live_game['away_team'], live_game['score'])
        if game: 
            games_changed.append(live_game) 
    if len(games_changed) != 0:
        send_email(games_changed)



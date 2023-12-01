from database.database import update_scores, update_table, update_round, get_rounds, update_rounds, update_game_time
from models.game import Game
from services.notification import notify_goal_on_bot
from services.scraping.table_scraping import scrap_table
from services.scraping.rounds_scraping import scrap_rounds
from core.config import initiate_database
from datetime import datetime
from utils import helper
from services.email_service import send_email, send_score_update_email
from services.scraping.live_games_scraping import scrap_live_games
from database.database import get_subscriptions

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
        game = await update_scores(live_game.home_team, live_game.away_team, live_game.score, live_game.time)
        if game:
            if live_game.score != 'Ainda não aconteceu!':
                games_changed.append(live_game)
        if live_game.time == 'FT':
            result = await update_game_time(live_game)
    if len(games_changed) != 0:
        notify_goal_on_bot(games_changed)
        recipients =  await get_recipients()
        send_score_update_email(games_changed, recipients)

async def get_recipients():
    subs = await get_subscriptions().to_list()
    return [sub.email for sub in subs if sub.confirmed]




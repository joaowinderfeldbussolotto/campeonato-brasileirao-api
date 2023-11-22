from database.database import update_table, update_round, get_rounds, update_rounds
from services.scraping.table_scraping import scrap_table
from services.scraping.rounds_scraping import scrap_rounds
from core.config import initiate_database
from datetime import datetime
from utils import helper
from services.email_service import send_email

async def init_rounds():
    rounds = scrap_rounds()
    await update_rounds(rounds)


async def populate_table():
    tournamente_table = scrap_table()
    await update_table(tournamente_table)

async def populate_rounds(scrapped_rounds):
    rounds = scrapped_rounds
    rounds_db = await get_rounds().to_list()
    rounds_to_update, games_changed = helper.find_different_rounds(rounds_db, rounds)
    if len(games_changed) != 0:
        send_email(games_changed)
    for r in rounds_to_update:
        print('updating rounds')
        await update_round(r)

async def populate_database():
    print(datetime.now())
    rounds = scrap_rounds()
    await initiate_database()
    await populate_table()
    await populate_rounds(rounds)


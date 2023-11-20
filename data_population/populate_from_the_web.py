from database.database import update_table, update_round, get_rounds
from services.scraping.table_scraping import scrap_table
from services.scraping.rounds_scraping import scrap_rounds
from core.config import initiate_database
from datetime import datetime
from utils import helper
async def populate_table():
    tournamente_table = scrap_table()
    await update_table(tournamente_table)

async def populate_rounds():
    rounds = scrap_rounds()
    rounds_db = await get_rounds().to_list()
    rounds_to_update = helper.find_different_rounds(rounds_db, rounds)
    for r in rounds_to_update:
        print('updating rounds')
        await update_round(r)

async def populate_database():
    print(datetime.now())
    await initiate_database()
    await populate_table()
    await populate_rounds()


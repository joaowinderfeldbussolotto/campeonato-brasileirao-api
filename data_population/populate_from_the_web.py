from database.database import update_table, save_rounds, update_rounds
from services.scraping.table_scraping import scrap_table
from services.scraping.rounds_scraping import scrap_rounds
from core.config import initiate_database

async def populate_table():
    tournamente_table = scrap_table()
    await update_table(tournamente_table)

async def populate_rounds():
    await initiate_database()

    rounds = scrap_rounds()
    await update_rounds(rounds)

async def populate_database():
    await initiate_database()
    await populate_table()
    await populate_rounds()


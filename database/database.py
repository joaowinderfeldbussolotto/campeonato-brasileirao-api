

from models.table import Table
from models.round import Round

table_collection = Table
round_collection = Round

async def delete_all_records(collection):
    await collection.all().delete()

async def update_table(table: [Table]):
    await delete_all_records(table_collection)
    for team in table:
        await team.create()

def get_table():
    return table_collection.all()

async def save_rounds(rounds):
    for new_round in rounds:
        await save_round(new_round)

async def save_round(new_round):
    return await new_round.create()

async def get_round(round_num):
    return await round_collection.find_one({"number": round_num})

def get_rounds():
    return round_collection.all()

async def update_rounds(rounds):
    await delete_all_records(round_collection)
    await save_rounds(rounds)
    print('Updated rounds')

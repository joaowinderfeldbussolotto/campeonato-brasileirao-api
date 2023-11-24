

from models.table import Table
from models.round import Round
from models.subscription import Subscription

table_collection = Table
round_collection = Round
subscription_collection = Subscription

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

async def update_round(round):
    update_dict = {k: v for k, v in round.dict().items() if k not in ["id", "revision_id"]}
    update_query = {"$set": {field: value for field, value in update_dict.items()}}
    db_round = await get_round(update_dict['number'])
    if db_round:
        await db_round.update(update_query)
        return db_round
    

async def update_scores(home_team_query: str, away_team_query: str, new_score: str):

    round_document = await round_collection.find_one(
        {
            'games': {
                '$elemMatch': {
                    'home_team': home_team_query,
                    'away_team': away_team_query,
                    'score': {'$ne': new_score}
                }
            }
        }
    )
    if round_document:
        games = round_document.games
        for i, game in enumerate(games):
            if game.home_team == home_team_query and game.away_team == away_team_query:
                break
        
        update_query = {"$set": {f"games.{i}.score": new_score}}
        
        await round_document.update(update_query)
        return True
    return False


async def get_subscription_by_email(email):
    return await subscription_collection.find_one({"email": email})
async def get_subscription_by_id(id):
    sub = await subscription_collection.get(id)
    return sub

def get_subscriptions():
    return subscription_collection.all()

async def save_subscription(subscription):
    return await subscription.create()

async def delete_subscription(id):
    sub = await get_subscription_by_id(id)
    if sub:
        return await sub.delete()

async def update_subscription(sub):
    update_query = {"$set": {field: value for field, value in dict(sub).items()}}

    return await sub.update(update_query)
from fastapi import APIRouter
from models.game import Game
from typing import List
from database.database import get_rounds 
router = APIRouter()

   
@router.get('/', 
            summary="Get live games",
            description="Retrieve live games from Brasileirão.",
            response_model = List[Game])

async def get_live_games():
    rounds = get_rounds()
    rounds = await rounds.to_list()
    live_games = [
        game_helper(game_data)
        for round_data in rounds
        for game_data in round_data.games
        if game_data.time != 'FT' and game_data.score != 'Ainda não aconteceu!'
    ]

    return live_games

def game_helper(game_data):
    game_data.time = 'Ao vivo'
    return game_data
from fastapi import APIRouter, status, Depends, HTTPException, Response
from models.round import Round
from models.game import Game
from typing import List
from services.scraping.rounds_scraping import scrap_rounds

router = APIRouter()

@router.get('/{num}', response_model = Round)
async def get_round(num: int):
    if not isinstance(num, int) or num < 0 or num > 38:
        raise HTTPException(detail = 'Por favor informe uma rodada válida: de 1 a 38', status_code = 400)
    return format_round(scrap_rounds().get(num), num)


def format_round(rounds, number):
    games = []
    for i in range(10):
        print(rounds['home'][i], rounds['away'][i], rounds['score'][i])
        home_team, away_team, score = rounds['home'][i], rounds['away'][i], rounds['score'][i]
        game = Game(home_team= home_team, away_team = away_team, score = score)
        games.append(game)

    return Round(number = number, games = games)
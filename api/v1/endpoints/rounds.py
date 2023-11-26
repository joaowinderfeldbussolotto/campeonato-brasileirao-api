from fastapi import APIRouter, status, Depends, HTTPException, Response
from models.round import RoundModel
from models.game import Game
from typing import List
from services.scraping.rounds_scraping import scrap_rounds
from database.database import get_round as get_round_db
router = APIRouter()

@router.get('/{num}', response_model = RoundModel)
async def get_round(num: int):
    if num < 0 or num > 38:
        raise HTTPException(detail = 'Por favor informe uma rodada válida: de 1 a 38', status_code = 400)
    round = await get_round_db(num)
    return round


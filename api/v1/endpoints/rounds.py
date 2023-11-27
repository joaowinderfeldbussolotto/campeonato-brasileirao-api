from fastapi import APIRouter, HTTPException
from models.round import RoundModel
from models.response import ErrorResponse
from database.database import get_round as get_round_db
router = APIRouter()

responses = ErrorResponse.get_default_responses()

@router.get('/{num}', 
            response_model=RoundModel,
            summary="Get Round Data",
            description="Retrieve data for a specific round.",
            responses = responses)

async def get_round(num: int):
    if num < 0 or num > 38:
        raise HTTPException(detail = 'Por favor informe uma rodada válida: de 1 a 38', status_code = 400)
    round = await get_round_db(num)
    return round


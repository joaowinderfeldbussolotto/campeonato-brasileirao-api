from typing import Optional
from pydantic import BaseModel, Field

class Game(BaseModel):
    home_team: str = Field(..., description="Nome do time da casa")
    away_team: str = Field(..., description="Nome do time visitante")
    score: str = Field(..., description="Placar no formato 'gols_time_casa x gols_time_visitante'")
    time: Optional[str] = Field(..., description="Minuto do jogo")


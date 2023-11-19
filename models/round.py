from typing import List

from pydantic import BaseModel, Field
from models.game import Game

class Round(BaseModel):
    number: int = Field(..., gt = -1, lt = 39)
    games : List[Game] = Field(...)
from typing import List
from beanie import Document
from bson import ObjectId

from pydantic import BaseModel, Field
from models.game import Game

class RoundModel(BaseModel):
    number: int = Field(..., gt = -1, lt = 39)
    games : List[Game] = Field(...)

class Round(Document, RoundModel):
    class Settings:
        name = 'round'

class RoundRequest(BaseModel):
    num: int = Field(..., gt = -1, lt = 39)

    

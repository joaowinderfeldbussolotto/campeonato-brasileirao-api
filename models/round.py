from typing import List
from beanie import Document
from bson import ObjectId

from pydantic import BaseModel, ConfigDict, Field
from models.game import Game

class Round(Document):
    number: int = Field(..., gt = -1, lt = 39)
    games : List[Game] = Field(...)
   
    class Settings:
        name = 'round'

  

    

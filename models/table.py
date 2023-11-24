from typing import Optional
from beanie import Document
from pydantic import BaseModel, Field

class TableModel(BaseModel):
    team: str = Field(...)
    position: int = Field(..., gt = 0, lt = 21)
    points: int = Field(..., gt = -1, lt = 115)
    games_played: int =  Field(..., gt = -1, lt = 39)

class Table(Document, TableModel):
    class Settings:
        name = 'table'

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
from fastapi import APIRouter, status, Depends, HTTPException, Response
from models.table import Table
from typing import List
from services.scraping.table_scraping import scrap_table

router = APIRouter()

@router.get('/', response_model = List[Table])
async def get_table():
    return scrap_table()
from fastapi import APIRouter, status, Depends, HTTPException, Response
from models.table import Table
from typing import List
from services.scraping.table_scraping import scrap_table
from database.database import get_table as get_table_db
router = APIRouter()

@router.get('/', response_model = List[Table])
async def get_table():
    table = get_table_db()
    table = await table.to_list()
    return table

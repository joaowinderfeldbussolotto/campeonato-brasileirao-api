from fastapi import APIRouter, status, Depends, HTTPException, Response
from models.table import TableModel
from typing import List
from database.database import get_table as get_table_db
router = APIRouter()

   
@router.get('/')
async def get_table(response_model = TableModel):
    table = get_table_db()
    table = await table.to_list()
    return format_table(table)

def format_table(table_document):
    return [TableModel(**dict(item)) for item in table_document]

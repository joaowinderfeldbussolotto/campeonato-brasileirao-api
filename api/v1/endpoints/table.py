from fastapi import APIRouter
from models.table import TableModel
from typing import List
from database.database import get_table as get_table_db
router = APIRouter()

   
@router.get('/', 
            summary="Get live standings",
            description="Retrieve standings from Brasileirão.",
            response_model = List[TableModel])
async def get_table():
    table = get_table_db()
    table = await table.to_list()
    return format_table(table)

def format_table(table_document):
    return [TableModel(**dict(item)) for item in table_document]

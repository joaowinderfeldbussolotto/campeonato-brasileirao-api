from fastapi import APIRouter
from api.v1.endpoints import table, rounds, subscription

api_router = APIRouter()
api_router.include_router(table.router, prefix = '/tabela', tags = ['tabela'])
api_router.include_router(rounds.router, prefix = '/rodada', tags = ['rodada'])
api_router.include_router(subscription.router, prefix ='/inscricao', tags = ['subscribe'])


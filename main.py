from fastapi import FastAPI

from core.config import settings, initiate_database
from api.v1.api import api_router
from data_population.populate_from_the_web import populate_database
app = FastAPI(title = 'API para jogos do Campeonato Brasileiro - Série A')
app.include_router(api_router, prefix = settings.API_V1_STR)

async def start_database():
    print('init database')
    await initiate_database()


app.add_event_handler('startup', start_database)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)

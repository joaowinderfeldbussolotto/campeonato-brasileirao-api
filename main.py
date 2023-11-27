from fastapi import FastAPI

from core.config import settings, initiate_database
from api.v1.api import api_router
from data_population.populate_from_the_web import populate_database, init_rounds
from aiocron import crontab
from exceptions.exception_handler import ExceptionHandler


app = FastAPI(title = 'API para jogos do Campeonato Brasileiro - Série A',
              description='This API provides information about games in the Campeonato Brasileiro - Serie A. '
                          'You can retrieve data about rounds, standings and matches. The data is regularly updated '
                          'from the web to ensure accuracy and relevance. You can also receive e-mails whenever a goal is scored!',
              version='1.0.0')


app.include_router(api_router, prefix = settings.API_V1_STR)
ExceptionHandler(app)
async def startup():
    print('init database')
    await initiate_database()
    await init_rounds()

@crontab("* * * * * */30", start=True)
async def scheduler_task():
    await populate_database()


app.add_event_handler('startup', startup)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)

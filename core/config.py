from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import models as models
from dotenv import load_dotenv
import os
load_dotenv()


class Settings():
    DATABASE_URL: Optional[str] = os.getenv('DATABASE_URL')
    API_V1_STR: str = '/api/v1'
    EMAIL_SENDER: str = os.getenv('EMAIL_SENDER')
    EMAIL_APP_PASSWORD: str = os.getenv('EMAIL_APP_PASSWORD')
    BOT_API_URL: str = os.getenv('BOT_API_URL')
    class Config:
        orm_mode = True


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(), document_models=models.__all__
    )

settings = Settings()
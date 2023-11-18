from fastapi import APIRouter

api_router = APIRouter()


@api_router.get('/')
async def root():
    return {"message": "Hello World!"}
from fastapi import APIRouter, BackgroundTasks , HTTPException, Request
from database.database import delete_subscription, get_subscription_by_email, get_subscription_by_id, save_subscription, update_subscription
from models.subscription import Subscription, UnsubscribeRequest
from models.response import Response
from services.email_service import send_confirm_email


router = APIRouter()

@router.get('/confirmacao/{id}', response_model = Response)
async def unsubscribe(id: str):
    response = await delete_subscription(id)
    message = 'Inscrição cancelada!'
    return Response(status_code = 201, message=message)

@router.post("/")
async def unsubscribe(request_data: UnsubscribeRequest,
                      request: Request, 
                      background_tasks: BackgroundTasks, 
                      response_model = Response):
    existing_subscription = await get_subscription_by_email(request_data.email)
    if not existing_subscription:
        raise HTTPException(status_code=400, detail="Email não encontrado")
    background_tasks.add_task(send_confirm_email, existing_subscription, request.url, 'Unsub')
    message =  "Foi encaminhado um email para confirmar desinscrição."
    return Response(status_code = 201, message=message)

from fastapi import APIRouter, BackgroundTasks , HTTPException, Request
from database.database import delete_subscription, get_subscription_by_email, save_subscription
from models.subscription import Subscription, UnsubscribeRequest
from fastapi.responses import JSONResponse

from services.email_service import send_confirm_unsub_email


router = APIRouter()

@router.post("/", response_model=Subscription)
async def subscribe(subscription: Subscription):
    existing_subscription = await get_subscription_by_email(subscription.email)
    if existing_subscription:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    new_subscription = Subscription(email = subscription.email, name = subscription.name)
    response = await save_subscription(new_subscription)
    return response

@router.get('/desinscrever/{id}')
async def unsubscribe(id: str):
    print(id)
    response = await delete_subscription(id)
    return {'message': 'Inscrição cancelada!'}


@router.post("/desinscrever/")
async def unsubscribe(request_data: UnsubscribeRequest, request: Request, background_tasks: BackgroundTasks):
    email = dict(request_data).get('email')
    existing_subscription = await get_subscription_by_email(email)
    if not existing_subscription:
        raise HTTPException(status_code=400, detail="Email não encontrado")
    background_tasks.add_task(send_confirm_unsub_email, existing_subscription, request.url)

    return {"message": "Foi encaminhado um email para confirmar desinscrição."}

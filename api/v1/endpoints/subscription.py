from fastapi import APIRouter, BackgroundTasks , HTTPException, Request
from database.database import delete_subscription, get_subscription_by_email, get_subscription_by_id, save_subscription, update_subscription
from models.subscription import Subscription, UnsubscribeRequest
from fastapi.responses import JSONResponse

from services.email_service import send_confirm_email


router = APIRouter()

@router.get("/confirmacao/{id}")
async def subscribe(id: str):
    existing_subscription = await get_subscription_by_id(id)
    if existing_subscription:
        print(existing_subscription)
        existing_subscription.confirmed = True
        response = await update_subscription(existing_subscription)
        print(response)
        return {'message': 'Inscrição confirmada'}


@router.post("/")
async def subscribe(subscription: Subscription, request: Request, background_tasks: BackgroundTasks):
    existing_subscription = await get_subscription_by_email(subscription.email)
    if existing_subscription:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    new_subscription = Subscription(email = subscription.email, name = subscription.name, verified = False)
    response = await save_subscription(new_subscription)
    background_tasks.add_task(send_confirm_email, new_subscription, request.url, 'Sub')

    return {'message': f'Foi encaminhado um email para {subscription.email} para confirmar inscrição'}


@router.get('/desinscrever/confirmacao/{id}')
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
    background_tasks.add_task(send_confirm_email, existing_subscription, request.url, 'Unsub')

    return {"message": "Foi encaminhado um email para confirmar desinscrição."}

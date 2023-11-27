from fastapi import APIRouter, BackgroundTasks , HTTPException, Request
from database.database import delete_subscription, get_subscription_by_email, get_subscription_by_id, save_subscription, update_subscription
from models.subscription import Subscription
from models.response import Response
from services.email_service import send_confirm_email
from models.response import ErrorResponse
responses = ErrorResponse.get_default_responses()

router = APIRouter()

@router.get("/confirmacao/{id}", 
            summary="Confirm subscription",
            description="Confirm your subscription to get emails about updates",
            responses =  {**responses, 404: {"description": "Not Found", "model": ErrorResponse}})

async def subscribe(id: str):
    existing_subscription = await get_subscription_by_id(id)
    if existing_subscription:
        existing_subscription.confirmed = True
        response = await update_subscription(existing_subscription)
        message = 'Inscrição confirmada'
        return Response(status_code = 200, message=message)
    return Response(status_code = 500, detail = "We were unable to confirm your subscription. The provided token were not found.")


@router.post("/", 
            summary="Request subscription",
            description="Request subscription to get emails about updates. You will receive an email to confirm it.",
             responses =  responses)

async def subscribe(subscription: Subscription, 
                    request: Request, 
                    background_tasks: BackgroundTasks):
    existing_subscription = await get_subscription_by_email(subscription.email)
    if existing_subscription:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    new_subscription = Subscription(email = subscription.email, name = subscription.name, verified = False)
    response = await save_subscription(new_subscription)
    background_tasks.add_task(send_confirm_email, new_subscription, request.url, 'Sub')
    message = f'Foi encaminhado um email para {subscription.email} para confirmar inscrição'
    return Response(status_code = 200, message=message)

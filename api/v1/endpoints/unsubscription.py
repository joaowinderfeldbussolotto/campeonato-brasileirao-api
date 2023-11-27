from fastapi import APIRouter, BackgroundTasks , HTTPException, Request
from database.database import delete_subscription, get_subscription_by_email,   update_subscription
from models.subscription import UnsubscribeRequest
from models.response import Response
from services.email_service import send_confirm_email
from models.response import ErrorResponse

responses = ErrorResponse.get_default_responses()
unsub_responses = {**responses, 404: {"description": "Not Found", "model": ErrorResponse}}

router = APIRouter()

@router.get('/confirmacao/{id}', 
            summary="Confirm unsubscription",
            description="Confirm your unsubscription to get emails about updates",
            responses =  unsub_responses)

async def unsubscribe(id: str):
    response = await delete_subscription(id)
    message = 'Inscrição cancelada!'
    return Response(status_code = 201, message=message)

@router.post("/",
            summary="Request unsubscription",
            description="Request unsubscription to stop receinving emails about updates. You will receive an email to confirm it.",
            responses =  unsub_responses)

async def unsubscribe(request_data: UnsubscribeRequest,
                      request: Request, 
                      background_tasks: BackgroundTasks 
                      ):
    existing_subscription = await get_subscription_by_email(request_data.email)
    if not existing_subscription:
        raise HTTPException(status_code=404, detail="Email não encontrado")
    background_tasks.add_task(send_confirm_email, existing_subscription, request.url, 'Unsub')
    message =  "Foi encaminhado um email para confirmar desinscrição."
    return Response(status_code = 201, message=message)

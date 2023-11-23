from fastapi import APIRouter , HTTPException
from database.database import get_subscription_by_email, save_subscription
from models.subscription import Subscription

router = APIRouter()

@router.post("/", response_model=Subscription)
async def subscribe(subscription: Subscription):
    existing_subscription = await get_subscription_by_email(subscription.email)
    if existing_subscription:
        raise HTTPException(status_code=400, detail="Email already subscribed")
    new_subscription = Subscription(email = subscription.email, name = subscription.name)
    response = await save_subscription(new_subscription)
    return response
from beanie import Document

from pydantic import EmailStr, BaseModel
from typing import Optional

class SubscriptionModel(BaseModel):
    email: EmailStr
    name: str
    confirmed: Optional[bool] = False

class Subscription(Document, SubscriptionModel):
    class Settings:
        name = 'subscriptions'

class UnsubscribeRequest(BaseModel):
    email: EmailStr
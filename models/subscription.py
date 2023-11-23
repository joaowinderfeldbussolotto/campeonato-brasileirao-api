from beanie import Document

from pydantic import EmailStr, BaseModel
from typing import Optional

class Subscription(Document):
    email: EmailStr
    name: str
    confirmed: Optional[bool] = False
    class Settings:
        name = 'subscriptions'

class UnsubscribeRequest(BaseModel):
    email: EmailStr
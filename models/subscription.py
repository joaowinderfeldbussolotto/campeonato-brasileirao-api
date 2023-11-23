from beanie import Document

from pydantic import EmailStr, BaseModel


class Subscription(Document):
    email: EmailStr
    name: str
    class Settings:
        name = 'subscriptions'

class UnsubscribeRequest(BaseModel):
    email: EmailStr
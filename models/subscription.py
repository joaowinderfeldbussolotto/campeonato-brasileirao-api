from beanie import Document

from pydantic import EmailStr


class Subscription(Document):
    email: EmailStr
    name: str
    class Settings:
        name = 'subscriptions'


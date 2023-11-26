from typing import Any
from pydantic import BaseModel

class Response(BaseModel):
    status_code: int
    message: str
    data: Any = [] 
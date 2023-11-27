from typing import Any, Union
from pydantic import BaseModel

class Response(BaseModel):
    status_code: int
    message: str
    data: Any = [] 

class ErrorResponse(BaseModel):
    detail: Union[str, list]
    status_code: int

    @classmethod
    def get_default_responses(cls):
        return {
            400: {"description": "Bad Request", "model": cls},
            422: {"description": "Validation Error", "model": cls},
            500: {"description": "Internal Server Error"}
        }

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.routing import RequestValidationError
from pydantic import ValidationError

class ExceptionHandler:
    def __init__(self, app):
        self.app = app
        self.app.add_exception_handler(RequestValidationError, ExceptionHandler.request_validation_exception_handler)
        self.app.add_exception_handler(ValidationError, ExceptionHandler.validation_exception_handler)
    
    @staticmethod
    async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        message = [ErrorHelper.get_error_message(err) for err in exc.errors()]
        return JSONResponse(status_code=422,
                            content={"detail": message})

    @staticmethod
    async def validation_exception_handler(request: Request, exc: ValidationError):
        return await ExceptionHandler.request_validation_exception_handler(request, exc)
    
    

class ErrorHelper:

    @staticmethod
    def get_error_message(error):
        loc = error.get('loc')
        field = ''
        if loc:
            field = f': {loc[1]}'
        return f'{error.get("msg")}{field}'


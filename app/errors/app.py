from werkzeug.exceptions import HTTPException

class AppError(HTTPException):
    def __init__(self, code, message=None):
        super().__init__(description=message)
        
        self.code = code
        if(message):
            self.message = message
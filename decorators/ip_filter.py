from flask import request
from decouple import config

from app.errors.app import AppError

def ip_filtered(f):
    def wrapper(*args, **kwargs):
        ip = request.remote_addr

        if ip not in config('ALLOWED_IPS').split(','):
            raise AppError(401,"Forbidden.")
        
        return f(*args, **kwargs)
    
    return wrapper
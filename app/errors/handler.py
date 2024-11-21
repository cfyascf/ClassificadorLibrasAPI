from flask import app, jsonify
from marshmallow import ValidationError

from app.errors.app import AppError

@app.errorhandler(AppError)
def handle_app_error(error):
    response = jsonify({
        "code": error.code,
        "message": error.message
    })

    response.status_code = error.code
    return response

@app.errorhandler(ValidationError)
def handle_app_error(error):
    response = jsonify({
        "code": error.code,
        "message": error.message
    })

    response.status_code = error.code
    return response
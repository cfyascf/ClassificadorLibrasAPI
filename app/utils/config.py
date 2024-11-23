from decouple import config

class Config:
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URI')
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
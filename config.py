import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
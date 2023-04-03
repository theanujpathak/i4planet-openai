import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or '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'
    UPLOADS_DEFAULT_DEST = os.path.join('/app', 'uploads')
    UPLOADS_DEFAULT_URL = 'http://localhost:5000/uploads/'
    UPLOADED_IMAGES_DEST = os.path.join(UPLOADS_DEFAULT_DEST, 'images')
    UPLOADED_IMAGES_URL = UPLOADS_DEFAULT_URL + 'images/'
    
    UPLOADED_FILES_ALLOW = ['png', 'jpg', 'jpeg', 'gif']

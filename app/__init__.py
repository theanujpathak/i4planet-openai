from flask import Flask
from config import Config
from flask_uploads import UploadSet, configure_uploads, IMAGES

images = UploadSet('images', IMAGES)

# images = UploadSet('images', IMAGES)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes.api import api
    app.register_blueprint(api)
    return app

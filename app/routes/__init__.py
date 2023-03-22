from flask import Blueprint

# Create a blueprint for the routes module
bp = Blueprint('api', __name__)

# Import the API routes
from .api import *


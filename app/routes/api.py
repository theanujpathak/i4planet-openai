from flask import Blueprint, request, jsonify
from app.models.openai_model import generate_text, get_openai_prediction

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return 'Welcome to the OpenAI API'

@api.route('/generate_text', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('input_text')
    response = generate_text(prompt)
    return jsonify({'text': response})

@api.route('/predict', methods=['POST'])
def predict():
    input_text = request.json.get('input_text')
    output_text = get_openai_prediction(input_text)
    return jsonify({'output_text': output_text})
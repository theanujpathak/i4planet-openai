from flask import Blueprint, request, jsonify
from app.models.openai_model import generate_text, get_openai_prediction, get_chat, edit_image, generate_image

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return 'Welcome to the i4planet OpenAI API'

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

@api.route('/chat', methods=['POST'])
def chat():
    input_text = request.json.get('input_text')
    output_text = get_chat(input_text)
    return jsonify({'output_text': output_text})

@api.route('/upload-image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})
    image = request.files['image']
    prompt = request.form['input_text']
    if image.filename == '':
        return jsonify({'error': 'No image selected'})
    image_data = edit_image(image, prompt)
    if 'image_url' in image_data:
        return jsonify({'success': True, 'image_path': image_data['image_url']})
    else:
        return jsonify({'error': image_data['error']})

@api.route('/generate-image', methods=['POST'])
def get_image():
    input_text = request.json.get('input_text')
    image_data = generate_image(input_text)
    if 'image_url' in image_data:
        return jsonify({'success': True, 'image_path': image_data['image_url']})
    else:
        return jsonify({'error': image_data['error']})
    return jsonify({'output_text': output_text})
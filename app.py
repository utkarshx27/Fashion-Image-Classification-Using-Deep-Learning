from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os
import json

from flask import render_template



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB limit

@app.route('/')
def home():
    return render_template('index.html')

# Load model and class labels
model = tf.keras.models.load_model('best_model.h5')
with open('class_labels.json', 'r') as f:
    class_names = json.load(f)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array / 255.0

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        
        # Preprocess and predict
        processed_img = preprocess_image(save_path)
        predictions = model.predict(processed_img)
        predicted_class = class_names[np.argmax(predictions)]
        confidence = float(np.max(predictions))

        print(type(predicted_class))
        if predicted_class == '0':
            pred_class_name = 'White Joggers'
        elif predicted_class == '1':
            pred_class_name = 'Black Joggers'
        elif predicted_class == '2':
            pred_class_name = 'Flat-Front Trousers with Drawstring Waist (maroon)'
        elif predicted_class == '3':
            pred_class_name = 'Relaxed Black Pure Linen Trousers'
        elif predicted_class == '4':
            pred_class_name = 'Black slim fit Pants'
        elif predicted_class == '5':
            pred_class_name = 'Something Crazy'
        else:
            pred_class_name = 'Unknown'

        if confidence < 0.5:
            predicted_class = 'unknown'
        print(predicted_class)
        print(confidence)
        return jsonify({
            'class': pred_class_name,
            'confidence': confidence
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
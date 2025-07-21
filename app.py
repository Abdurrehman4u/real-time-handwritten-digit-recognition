from flask import Flask, render_template, request, jsonify
import os
import numpy as np
from PIL import Image
import tensorflow as tf
from utils.predictor import predict_digit
from utils.database import init_db, save_prediction, get_predictions
import io
import base64
import uuid
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Initialize database
init_db()

# Load the model
model = tf.keras.models.load_model("model/handwritten.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename:
                # Generate unique filename
                file_extension = file.filename.rsplit('.', 1)[1].lower()
                unique_filename = f"{uuid.uuid4()}.{file_extension}"
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                
                file.save(file_path)
                img = Image.open(file_path)
                result, confidence = predict_digit(img, model)
                
                # Save to database
                prediction_id = save_prediction('upload', result, confidence, file_path)
                
                return jsonify({
                    'prediction': str(result),
                    'confidence': f"{confidence:.2f}%",
                    'image_path': file_path,
                    'id': prediction_id
                })

        elif 'canvas_data' in request.form:
            canvas_data = request.form['canvas_data']
            img = Image.open(io.BytesIO(base64.b64decode(canvas_data.split(',')[1])))
            
            # Save canvas image
            canvas_filename = f"canvas_{uuid.uuid4()}.png"
            canvas_path = os.path.join(app.config['UPLOAD_FOLDER'], canvas_filename)
            img.save(canvas_path)
            
            result, confidence = predict_digit(img, model)
            
            # Save to database
            prediction_id = save_prediction('canvas', result, confidence, canvas_path)
            
            return jsonify({
                'prediction': str(result),
                'confidence': f"{confidence:.2f}%",
                'id': prediction_id
            })

        return jsonify({'error': 'No valid input provided'})
    
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return jsonify({'error': 'An error occurred during prediction'})

@app.route('/history')
def history():
    """Display prediction history page"""
    try:
        predictions = get_predictions()
        print(f"Retrieved {len(predictions)} predictions") # Debug log
        return render_template('history.html', predictions=predictions)
    except Exception as e:
        print(f"Error in history: {str(e)}")
        return render_template('history.html', predictions=[], error="Failed to load history")

if __name__ == '__main__':
    # Create upload directory if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host='0.0.0.0', port=8000, debug=True)

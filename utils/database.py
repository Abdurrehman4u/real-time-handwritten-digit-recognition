import sqlite3
import uuid
from datetime import datetime
import os

def init_db():
    """Initialize the database and create tables if they don't exist"""
    if not os.path.exists('database'):
        os.makedirs('database')
    
    conn = sqlite3.connect('database/predictions.db')
    cursor = conn.cursor()
    
    # Drop existing table to recreate with correct schema
    cursor.execute('DROP TABLE IF EXISTS predictions')
    
    cursor.execute('''
        CREATE TABLE predictions (
            id TEXT PRIMARY KEY,
            input_type TEXT NOT NULL,
            predicted_digit INTEGER NOT NULL,
            confidence REAL NOT NULL,
            image_path TEXT,
            timestamp TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def save_prediction(input_type, predicted_digit, confidence, image_path=None):
    """Save prediction result to database"""
    conn = sqlite3.connect('database/predictions.db')
    cursor = conn.cursor()
    
    prediction_id = str(uuid.uuid4())[:8]  # Short ID for display
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Ensure predicted_digit is an integer
    predicted_digit = int(predicted_digit)
    confidence = float(confidence)
    
    cursor.execute('''
        INSERT INTO predictions (id, input_type, predicted_digit, confidence, image_path, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (prediction_id, input_type, predicted_digit, confidence, image_path, timestamp))
    
    conn.commit()
    conn.close()
    
    print(f"Saved prediction - ID: {prediction_id}, Digit: {predicted_digit}, Confidence: {confidence}")
    return prediction_id

def get_predictions():
    """Get all predictions from database"""
    conn = sqlite3.connect('database/predictions.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, input_type, predicted_digit, confidence, image_path, timestamp
        FROM predictions
        ORDER BY timestamp DESC
    ''')
    
    predictions = cursor.fetchall()
    conn.close()
    
    return predictions
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
    
    # Create the table only if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id TEXT PRIMARY KEY,
            input_type TEXT NOT NULL,
            predicted_digit TEXT NOT NULL,  -- Changed from INTEGER to TEXT to handle "Uncertain"
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
    
    # Handle both integer digits and "Uncertain" string
    if predicted_digit == "Uncertain":
        predicted_digit_str = "Uncertain"
    else:
        predicted_digit_str = str(int(predicted_digit))
    
    confidence = float(confidence)
    
    cursor.execute('''
        INSERT INTO predictions (id, input_type, predicted_digit, confidence, image_path, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (prediction_id, input_type, predicted_digit_str, confidence, image_path, timestamp))
    
    conn.commit()
    conn.close()
    
    print(f"Saved prediction - ID: {prediction_id}, Digit: {predicted_digit_str}, Confidence: {confidence}")
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
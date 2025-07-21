# Real Time Handwritten Digit Recognition Flask Application

This project is a Flask web application that allows users to recognize handwritten digits. Users can either upload an image of a handwritten digit or draw it directly on a canvas. The application utilizes a pre-trained Keras model to predict the digit and displays the result in real-time.

## Project Structure

```
handwritten-digit-recognition-flask
├── app.py                     # Main entry point of the Flask application
├── static
│   ├── css
│   │   └── style.css          # CSS styles for the web application
│   ├── js
│   │   └── script.js          # JavaScript for client-side functionality
│   └── uploads                # Directory for temporarily storing uploaded images
├── templates
│   └── index.html             # Main HTML template for the application
├── model
│   └── handwritten.h5         # Trained Keras model for handwritten digit recognition
├── prediction                 # Directory for storing prediction results
├── utils
│   └── predictor.py           # Utility functions for loading the model and making predictions
├── requirements.txt           # Python dependencies required for the project
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone https://github.com/Abdurrehman4u/real-time-handwritten-digit-recognition.git
   cd handwritten-digit-recognition-flask
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- **Upload an Image**: Click on the upload button to select an image of a handwritten digit from your device.
- **Draw on Canvas**: Use the drawing canvas to sketch a digit. Adjust the stroke width as needed.
- **Predict**: Click the "Predict" button to see the predicted digit based on your input.


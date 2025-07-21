# Real-Time Handwritten Digit Recognition Flask Application

This project is a Flask web application that allows users to recognize handwritten digits. Users can either upload an image of a handwritten digit or draw it directly on a canvas. The application utilizes a pre-trained Keras model to predict the digit and displays the result along with the confidence score. All predictions are stored in an SQLite database, and users can view the prediction history.

## Project Features

- **Upload an Image**: Users can upload an image of a handwritten digit for recognition.
- **Draw on Canvas**: Users can draw a digit directly on the canvas for recognition.
- **Real-Time Prediction**: The application predicts the digit and displays the confidence score in real-time.
- **Prediction History**: All predictions (including input type, timestamp, and confidence) are stored in an SQLite database and can be viewed in a separate history page.
- **Image Previews**: Uploaded images and canvas drawings are saved and displayed in the history page.

## Project Structure

```
handwritten-digit-recognition-flask
├── app.py                     # Main entry point of the Flask application
├── static
│   ├── css
│   │   ├── style.css          # CSS styles for the main application
│   │   └── history.css        # CSS styles for the history page
│   ├── js
│   │   ├── script.js          # JavaScript for client-side functionality
│   │   └── history.js         # JavaScript for the history page
│   └── uploads                # Directory for storing uploaded and canvas images
├── templates
│   ├── index.html             # Main HTML template for the application
│   └── history.html           # HTML template for the prediction history page
├── model
│   └── handwritten.h5         # trained Keras model for handwritten digit recognition
├── database
│   └── predictions.db         # SQLite database for storing prediction history
├── utils
│   ├── predictor.py           # Utility functions for loading the model and making predictions
│   └── database.py            # Utility functions for database initialization and operations
├── requirements.txt           # Python dependencies required for the project
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Abdurrehman4u/real-time-handwritten-digit-recognition.git
   cd handwritten-digit-recognition-flask
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- **Upload an Image**: Click on the upload button to select an image of a handwritten digit from your device.
- **Draw on Canvas**: Use the drawing canvas to sketch a digit. Click "Clear Canvas" to reset the canvas.
- **Predict**: Click the "Predict" button to see the predicted digit and confidence score.
- **View History**: Click the "View Prediction History" button to navigate to the history page, where you can see all past predictions along with input images, timestamps, and confidence scores.

## Dependencies

The project requires the following Python packages:
- Flask
- TensorFlow
- Pillow
- NumPy
- Matplotlib
- OpenCV
- Werkzeug
- UUID (for generating unique IDs)

All dependencies are listed in the `requirements.txt` file.

## Database

The application uses SQLite (built into Python) to store prediction history. The database schema includes:
- **ID**: A unique identifier for each prediction.
- **Input Type**: Either "canvas" or "upload".
- **Predicted Digit**: The digit predicted by the model.
- **Confidence**: The confidence score of the prediction.
- **Image Path**: The file path of the input image.
- **Timestamp**: The date and time of the prediction.

## Additional Features

- **Responsive Design**: The application is mobile-friendly and adapts to different screen sizes.
- **Error Handling**: Displays appropriate error messages for invalid inputs or server issues.
- **Image Previews**: Uploaded and canvas images are saved and displayed in the history page.

## Future Enhancements

- Add support for multi-digit recognition.
- Improve the UI/UX for better user interaction.
- Add user authentication to track predictions per user.


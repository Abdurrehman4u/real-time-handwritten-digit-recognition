import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

def load_model():
    model = tf.keras.models.load_model("model/handwritten.h5")
    return model

def predict_digit(image, model):
    image = ImageOps.grayscale(image)
    img = image.resize((28, 28))
    img = np.array(img, dtype='float32')
    img = img / 255
    img = img.reshape((1, 28, 28, 1))
    pred = model.predict(img)
    result = np.argmax(pred[0])
    confidence = float(np.max(pred[0]) * 100)  # Convert to percentage
    
    # Convert 0-9 to 1-10 range
    if result == 0:
        display_result = 10  # Map 0 to 10
    else:
        display_result = result  # 1-9 stay the same
    
    print(f"Model prediction: {result}, Display result: {display_result}, Confidence: {confidence:.2f}%")
    return int(display_result), confidence  # Ensure it's an integer
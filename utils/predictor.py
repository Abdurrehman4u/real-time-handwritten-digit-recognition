import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np


def predict_digit(image, model):
    image = ImageOps.grayscale(image)
    img = image.resize((28, 28))
    img = np.array(img, dtype='float32')
    img = img / 255
    img = img.reshape((1, 28, 28, 1))
    pred = model.predict(img)
    for i, p in enumerate(pred[0]):
        print(f"Class {i}: {p:.2f}")
    result = np.argmax(pred[0])
    confidence = float(np.max(pred[0]) * 100)  # Convert to percentage

    # Check if confidence is below 90%
    if confidence < 90.0:
        print(f"Model prediction: {result}, Display result: Uncertain (confidence too low), Confidence: {confidence:.2f}%")
        return "Uncertain", confidence
    else:
        print(f"Model prediction: {result}, Display result: {result}, Confidence: {confidence:.2f}%")
        return int(result), confidence
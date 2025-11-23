import numpy as np
from PIL import Image
import tensorflow as tf
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "models" / "model_epoch_12.keras"
IMG_SIZE = (224, 224)

LABELS = ["Cloudy", "Rain", "Shine", "Sunrise"]

def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

def preprocess(img: Image.Image):
    img = img.resize(IMG_SIZE)
    img = np.array(img).astype('float32') / 255.0
    if img.shape[-1] == 4:  # RGBA → RGB
        img = img[..., :3]
    return np.expand_dims(img, 0)

def predict(model, img):
    tensor = preprocess(img)
    preds = model.predict(tensor)[0]
    idx = np.argmax(preds)
    return LABELS[idx], preds[idx], preds


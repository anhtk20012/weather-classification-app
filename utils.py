import numpy as np
from PIL import Image
import tensorflow as tf
from pathlib import Path
from huggingface_hub import hf_hub_download

path_file = Path(__file__).parent / "models" / "model_epoch_12.keras"
img_size = (224, 224)

LABELS = ["Cloudy", "Rain", "Shine", "Sunrise"]

def load_model():
    try:
        model = tf.keras.models.load_model(path_file)
    except Exception:
        path_file.parent.mkdir(parents=True, exist_ok=True)
        hf_hub_download(
            repo_id="tronganhwork/weather-classification-app",
            filename="model_epoch_12.keras",
            local_dir=path_file.parent,
            local_dir_use_symlinks=False,
        )
        model = tf.keras.models.load_model(path_file)
    return model

def preprocess(img: Image.Image):
    img = img.resize(img_size)
    img = np.array(img).astype('float32') / 255.0
    if img.shape[-1] == 4:  # RGBA → RGB
        img = img[..., :3]
    return np.expand_dims(img, 0)

def predict(model, img):
    tensor = preprocess(img)
    preds = model.predict(tensor)[0]
    idx = np.argmax(preds)
    return LABELS[idx], preds[idx], preds


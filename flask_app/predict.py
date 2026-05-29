from .load_model import get_model_version_details
from .utils import normalize_text
from src.logger import logging

def predict(text):
    """Predict whether the input text is spam or not."""
    try:
        model, vectorizer = get_model_version_details("my_model")
        normalized_text = normalize_text(text)
        text_vector = vectorizer.transform([normalized_text])
        prediction = model.predict(text_vector)[0]
        probability = model.predict_proba(text_vector)[0]
        return prediction, probability
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        raise
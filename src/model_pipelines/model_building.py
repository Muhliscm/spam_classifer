import numpy as np

import pickle
from sklearn.naive_bayes import MultinomialNB
from src.logger import logging
from src.utils.data_loaders import load_data
from src.utils.yaml import load_params

def train_model(X_train: np.ndarray, y_train: np.ndarray,nb_alpha: float) -> MultinomialNB:
    """Train the Multinomial Naive Bayes model."""
    try:
        clf = MultinomialNB(alpha=nb_alpha)  # You can adjust the alpha parameter as needed
        clf.fit(X_train, y_train)
        logging.info('Model training completed')
        return clf
    except Exception as e:
        logging.error('Error during model training: %s', e)
        raise

def save_model(model, file_path: str) -> None:
    """Save the trained model to a file."""
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(model, file)
        logging.info('Model saved to %s', file_path)
    except Exception as e:
        logging.error('Error occurred while saving the model: %s', e)
        raise

def main():
    try:

        train_data = load_data('./data/processed/train_tfidf.csv')
        X_train = train_data.iloc[:, :-1].values
        y_train = train_data.iloc[:, -1].values

        params = load_params('params.yaml')
        nb_alpha = params['model_training']['nb_alpha']

        clf = train_model(X_train, y_train, nb_alpha=nb_alpha)

        save_model(clf, 'models/model.pkl')
        logging.info('Model training completed successfully')
    except Exception as e:
        logging.error('Failed to complete the model building process: %s', e)
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
# feature engineering
import numpy as np
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from src.logger import logging
import pickle
from src.utils.yaml import load_params
from src.utils.data_loaders import load_data


def apply_tfidf(train_data: pd.DataFrame, test_data: pd.DataFrame, max_features: int, ngram_range: tuple) -> pd.DataFrame:
    """Apply Tfidf Vectorizer to the data."""
    try:
        logging.info("Applying Tfidf...")
        
        vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=ngram_range)

        train_data = train_data[~train_data['text'].isnull()]
        test_data = test_data[~test_data['text'].isnull()]

        X_train = train_data['text'].values
        y_train = train_data['target'].values
        X_test = test_data['text'].values
        y_test = test_data['target'].values
       

        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)

        train_df = pd.DataFrame(X_train_tfidf.toarray())
        train_df['label'] = y_train

        test_df = pd.DataFrame(X_test_tfidf.toarray())
        test_df['label'] = y_test

        pickle.dump(vectorizer, open('models/vectorizer.pkl', 'wb'))
        logging.info('Tfidf applied and data transformed')

        return train_df, test_df
    except Exception as e:
        logging.error('Error during Tfidf transformation: %s', e)
        raise

def save_data(df: pd.DataFrame, file_path: str) -> None:
    """Save the dataframe to a CSV file."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_csv(file_path, index=False)
        logging.info('Data saved to %s', file_path)
    except Exception as e:
        logging.error('Unexpected error occurred while saving the data: %s', e)
        raise

def main():
    try:
        params = load_params('params.yaml')
        max_features = params['feature_engineering']['max_features']
        ngram_range = tuple(params['feature_engineering']['ngram_range'])
        # max_features = 20

        train_data = load_data('./data/interim/train_processed.csv')
        test_data = load_data('./data/interim/test_processed.csv')

        train_df, test_df = apply_tfidf(train_data, test_data, max_features, ngram_range)

        save_data(train_df, os.path.join("./data", "processed", "train_tfidf.csv"))
        save_data(test_df, os.path.join("./data", "processed", "test_tfidf.csv"))
    except Exception as e:
        logging.error('Failed to complete the feature engineering process: %s', e)
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
import pandas as pd
import pickle
import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string


def load_model():
    try:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)

        with open('vectorizer.pkl', 'rb') as f:
            ifidf = pickle.load(f)

    except Exception as ex:
        print(f"Exception ex:{ex} occurred in loading model")
        raise (ex)
    return model, ifidf


def transformation(text):
    ps = PorterStemmer()

    # lower text
    text = text.lower()
    # convert into words
    text = nltk.word_tokenize(text)

    # removing special characters
    y = []
    for str_ in text:
        if str_.isalnum():
            y.append(str_)

    text = y.copy()
    y.clear()

    # removing stop words and punctuation
    for str_ in text:
        if str_ not in stopwords.words('english') and str_ not in string.punctuation:
            y.append(str_)

    text = y.copy()
    y.clear()

    # stemming
    for str_ in text:
        y.append(ps.stem(str_))

    return " ".join(y)


def predict(data):
    model, tfidf = load_model()
    data = transformation(data)
    data = tfidf.transform([data])
    prediction = model.predict(data)
    probability = model.predict_proba(data)
    probability = np.ravel(probability)
    return prediction, probability

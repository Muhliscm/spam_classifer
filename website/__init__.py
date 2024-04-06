from flask import Flask
from .views import views
import pandas as pd
import pickle


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "my_key"
    app.register_blueprint(views, url_prefix="/")

    return app


# def load_data_and_model():
#     try:
#         df = pd.read_csv('for_prediction.csv')
#         with open('model.pkl', 'rb') as f:
#             model = pickle.load(f)
#     except Exception as ex:
#         print(f"Exception {ex} occurred in loading data")
#         raise (ex)
#     return df, model

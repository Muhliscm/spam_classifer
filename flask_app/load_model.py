from flask import Flask, render_template, request
import mlflow
import os
import pandas as pd
import joblib
import pickle
# from prometheus_client import Counter, Histogram, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST

from src.utils.mlflow import setup_mlflow_tracking
from src.logger import logging
from src.constants import MODEL_CACHE_PATH


setup_mlflow_tracking()
client = mlflow.MlflowClient()

model_name = "my_model"

def get_latest_model_version(model_name):
    try:
        # Check MLflow version
        import mlflow
        mlflow_version = int(mlflow.__version__.split('.')[0])

        if mlflow_version >= 3:
            # MLflow 3.x — use alias
            try:
                version = client.get_model_version_by_alias(
                    model_name, "production"
                )
                return version.version, "alias"
            except Exception:
                # No alias set — fall back to latest version
                versions = client.search_model_versions(
                    f"name='{model_name}'"
                )
                latest = max(versions, key=lambda v: int(v.version))
                return latest.version, "version"
        else:
            # MLflow 2.x — use stages
            versions = client.get_latest_versions(
                model_name, stages=["Production"]
            )
            if not versions:
                versions = client.get_latest_versions(
                    model_name, stages=["None"]
                )
            return versions[0].version, "version"

    except Exception as e:
        logging.error(f"Error fetching model version: {e}")
        raise


def get_model_version_details(model_name):
    model_version, source = get_latest_model_version(model_name)

    if not model_version:
        raise ValueError(f"No versions found for model: {model_name}")

    # Build correct URI based on source
    if source == "alias":
        model_uri = f"models:/{model_name}@production"
    else:
        model_uri = f"models:/{model_name}/{model_version}"

    # Check if model already downloaded
    if os.path.exists(MODEL_CACHE_PATH):
        logging.info("Loading model from local cache...")
        model = joblib.load(MODEL_CACHE_PATH)   # instant! ✅
    else:
        logging.info("Downloading model from MLflow...")
        model = mlflow.sklearn.load_model(
            f"models:/{model_name}/{model_version}"
        )
        # Save locally for next time
        joblib.dump(model, MODEL_CACHE_PATH)
        logging.info("Model cached locally!")
    vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))
    return model, vectorizer


if __name__=='__main__':
    model, vectorizer = get_model_version_details("my_model")
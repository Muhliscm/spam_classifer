FROM python:3.10-slim

WORKDIR /app

# Step 1: Copy requirements FIRST (better layer caching)
COPY flask_app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 2: Download NLTK data
RUN python -m nltk.downloader stopwords wordnet

# Step 3: Copy application code
COPY flask_app/ /app/flask_app/
COPY src/ /app/src/
COPY app.py /app/app.py

# Step 4: Copy models if exists
COPY models/ /app/models/

# Environment
ENV PYTHONPATH=/app
ENV FLASK_ENV=production

EXPOSE 5000

# Production server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]

# test server
# CMD ["python3", "-m", "flask_app.app"]

import joblib
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define model file paths
SCORING_MODEL_PATH = 'anomaly_model_detection_anomalies.pkl'
ANOMALY_MODEL_PATH = 'anomaly_model_scoring_credit.pkl'

try:
    # Load models
    rf_model = joblib.load(SCORING_MODEL_PATH)
    iso_model = joblib.load(ANOMALY_MODEL_PATH)

# Handle case where models are not found
except FileNotFoundError as e:
    rf_model = None
    iso_model = None
# Handle other exceptions during model loading   
except Exception as e:
    rf_model = None
    iso_model = None

# Define a simple route to check if the API is running
@app.route('/', methods=['GET'])
def ping():
    return "API is running"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
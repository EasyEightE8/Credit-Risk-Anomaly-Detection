import joblib
import os
from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__)

# Define model file paths
SCORING_MODEL_PATH = 'models/anomaly_model_scoring_credit.pkl'
ANOMALY_MODEL_PATH = 'models/anomaly_model_detection_anomalies.pkl'

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
    if rf_model and iso_model:
        return jsonify({ "status": "online", "message": "Modèles chargés." })
    else:
        return jsonify({ "status": "offline", "message": "Modèles non chargés." }), 500

# Define a route for scoring
@app.route('/score', methods=['POST'])
# Scoring endpoint
def score():
    # Check if models are loaded
    if not rf_model or not iso_model:
        return jsonify({"error": "Modèles non chargés."}), 500
    
    # Parse input data
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        df_input = pd.DataFrame([data])
        
        features_scoring = ['loan_amount', 'term_months', 'interest_rate', 'borrower_age', 'borrower_income', 'credit_score']
        df_input_scoring = df_input[features_scoring]
        
        features_anomalie = ['loan_amount', 'interest_rate', 'borrower_income', 'credit_score']
        df_input_anomalie = df_input[features_anomalie]
        
    except KeyError as e:
        return jsonify({"error": f"Missing features in input data: {e}"}), 400
    except Exception as e:
        return jsonify({"error": "Error processing input data"}), 500 

    # Convert input data to DataFrame
    try:
        proba_defaut = rf_model.predict_proba(df_input_scoring)[0][1]
        
        prediction_anomalie = iso_model.predict(df_input_anomalie)[0]
        
        is_anomaly = 1 if prediction_anomalie == -1 else 0
        
    except Exception as e:
        return jsonify({"error": "Error during model prediction"}), 500
 
    
    return jsonify({
        "probability_default": rf_model.predict_proba(df_input_scoring)[:, 1].tolist(),
        "is_anomaly": int(is_anomaly)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
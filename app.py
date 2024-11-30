from flask import Flask, request, jsonify
import pickle
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import os

app = Flask(__name__)

# Load the trained model
with open('sarimax_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    year = data.get('year')
    month = data.get('month')

    # Create a date range for the prediction
    forecast_date = pd.date_range(start=f'{year}-{month:02d}-01', end=f'{year}-{month:02d}-01', freq='MS')

    # Make a prediction
    prediction = model.forecast(steps=1, index=forecast_date)

    return jsonify({'prediction': prediction.iloc[0]})

if __name__ == '__main__':
    app.run(debug=True)
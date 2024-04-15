# app.py

from flask import Flask, request, jsonify, send_file
import pandas as pd  # Import pandas here
import io
import matplotlib.pyplot as plt
from config import DATA_FILE_PATH, API_PORT, DEBUG_MODE, SARIMA_ORDER, SEASONAL_ORDER
from utils import load_data, split_data
from model_training import train_sarima_model, forecast


from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

# Existing code...


# Load the data
data = load_data(DATA_FILE_PATH)
# Here we make sure pandas is imported to use to_datetime and to_period
train_data, test_data = split_data(data, pd.to_datetime("2021-01-01").to_period('M'))

# Train model
model_fit = train_sarima_model(train_data, SARIMA_ORDER, SEASONAL_ORDER)

@app.route('/forecast', methods=['GET'])
def get_forecast():
    # Ensure the index is in timestamp for prediction compatibility
    if isinstance(test_data.index, pd.PeriodIndex):
        test_data.index = test_data.index.to_timestamp()

    predictions = forecast(model_fit, test_data)
    # Format the predictions to link them with their corresponding dates
    results = [{'date': str(date), 'forecast': float(pred)} for date, pred in zip(test_data.index, predictions)]
    return jsonify(results)

@app.route('/plot')
def plot_data():
    fig, ax = plt.subplots()
    ax.plot(test_data.index.to_timestamp(), forecast(model_fit, test_data), 'r-', label='Forecasted Sales')
    ax.set_title('Sales Forecast')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return send_file(buf, mimetype='image/png', as_attachment=True, attachment_filename='forecast.png')

if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, port=API_PORT)

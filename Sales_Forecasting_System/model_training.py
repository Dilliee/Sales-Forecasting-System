# model_training.py

import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt


def train_sarima_model(train_data, order, seasonal_order):
    """
    Trains a SARIMA model on the provided training data.

    Parameters:
        train_data (DataFrame): The training data with a datetime index and a 'Sales' column.
        order (tuple): The (p, d, q) order of the model.
        seasonal_order (tuple): The (P, D, Q, s) seasonal order of the model.

    Returns:
        model_fit (SARIMAXResults): The trained model object.
    """
    # Fit the SARIMA model
    model = SARIMAX(train_data['Sales'], order=order, seasonal_order=seasonal_order)
    model_fit = model.fit(disp=False)  # Set disp=True to see convergence messages

    return model_fit


# model_training.py
def forecast(model_fit, test_data):
    if test_data.empty:
        print("Test data set is empty. No predictions to make.")
        return None
    start = test_data.index[0]
    end = test_data.index[-1]
    predictions = model_fit.predict(start=start, end=end, dynamic=True)
    return predictions

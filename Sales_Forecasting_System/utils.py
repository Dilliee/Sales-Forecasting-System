# utils.py

import pandas as pd

def load_data(filepath):
    """Load data from a CSV file and return as DataFrame."""
    return pd.read_csv(filepath)

def split_data(data, split_date):
    """Split data into training and testing sets based on a date."""
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    data.index = pd.DatetimeIndex(data.index).to_period('M')

    train_data = data[data.index < split_date]
    test_data = data[data.index >= split_date]
    return train_data, test_data

# data_preprocessing.py

import pandas as pd

def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    # Explicitly set the frequency of the DateTimeIndex to 'M' for monthly data
    data.index = data.index.to_period('M')

    data.ffill(inplace=True)

    split_date = pd.to_datetime("2021-01-01").to_period('M')
    train_data = data[data.index < split_date]
    test_data = data[data.index >= split_date]

    return train_data, test_data

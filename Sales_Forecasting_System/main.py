# main.py

import pandas as pd  # Ensure Pandas is imported
from data_preprocessing import load_and_preprocess_data
from model_training import train_sarima_model, forecast
import matplotlib.pyplot as plt

def main():
    data_filepath = "C:\\Users\\Admin\\Documents\\Spreadsheets\\Sheets\\sample_sales_data.csv"
    train_data, test_data = load_and_preprocess_data(data_filepath)

    if test_data.empty:
        print("No test data available. Check your data range and split logic.")
        return  # Exit the function if there is no test data

    order = (1, 1, 0)
    seasonal_order = (0, 1, 0, 12)
    model_fit = train_sarima_model(train_data, order, seasonal_order)
    predictions = forecast(model_fit, test_data)

    if predictions is not None:
        # Check if the index needs conversion
        if isinstance(train_data.index, pd.PeriodIndex):
            train_data.index = train_data.index.to_timestamp()
            test_data.index = test_data.index.to_timestamp()

        plt.figure(figsize=(10, 5))
        plt.plot(train_data.index, train_data['Sales'], label='Train Sales')
        plt.plot(test_data.index, test_data['Sales'], label='Actual Sales')
        plt.plot(test_data.index, predictions, label='Forecasted Sales', color='red')
        plt.title('Sales Forecast vs Actuals')
        plt.xlabel('Date')
        plt.ylabel('Sales')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    main()

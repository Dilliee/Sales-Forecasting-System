# config.py

# File Paths
DATA_FILE_PATH = "C:\\Users\\Admin\\Documents\\Spreadsheets\\Sheets\\sample_sales_data.csv"
MODEL_SAVE_PATH = "C:\\Users\\Admin\\Documents\\Spreadsheets\\New_Sheets"

# Model Parameters
SARIMA_ORDER = (1, 1, 0)
SEASONAL_ORDER = (0, 1, 0, 12)

# API Configuration
API_PORT = 5000
DEBUG_MODE = True

# Database Configuration (Example)
DATABASE_URI = "mysql://user:password@localhost/mydatabase"

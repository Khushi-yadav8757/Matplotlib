# Fetching Data
#Data can come from multiple sources:

a) CSV / Excel File
import pandas as pd

# CSV
data = pd.read_csv('sales_data.csv')

# Excel
# data = pd.read_excel('sales_data.xlsx')

print(data.head())  # See first 5 rows

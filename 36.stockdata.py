import pandas as pd
import numpy as np

# Load the stock data from CSV
data = pd.read_csv('stock_data.csv')

# Convert the 'Date' column to a datetime type and set it as the index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Calculate daily price change and percent change
data['DailyChange'] = data['Close'].diff()
data['PercentChange'] = data['Close'].pct_change() * 100

# Calculate variability measures
mean_daily_change = data['DailyChange'].mean()
std_daily_change = data['DailyChange'].std()
mean_percent_change = data['PercentChange'].mean()
std_percent_change = data['PercentChange'].std()

# Insights into stock price movements
print(f"Mean Daily Change: {mean_daily_change:.2f}")
print(f"Standard Deviation of Daily Change: {std_daily_change:.2f}")
print(f"Mean Percent Change: {mean_percent_change:.2f}%")
print(f"Standard Deviation of Percent Change: {std_percent_change:.2f}%")

# Identify days with extreme price changes
extreme_changes = data[(data['DailyChange'] > 2 * std_daily_change) | (data['DailyChange'] < -2 * std_daily_change)]
print("Days with Extreme Price Changes:")
print(extreme_changes[['Close', 'DailyChange', 'PercentChange']])

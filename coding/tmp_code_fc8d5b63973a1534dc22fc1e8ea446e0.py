import pandas as pd

# Define the tickers
tickers = ['META', 'TSLA']

# Get the historical data for each ticker using pandas_datareader
data = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=META&apikey=YOUR_API_KEY')

# Convert the date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Set the date as the index
data.set_index('Date', inplace=True)

# Calculate the year-to-date gain
year_to_date_gain_meta = (data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0]
year_to_date_gain_tsla = (data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0]

print(f"Year-to-date gain for META: {year_to_date_gain_meta:.2%}")
print(f"Year-to-date gain for TSLA: {year_to_date_gain_tsla:.2%}")
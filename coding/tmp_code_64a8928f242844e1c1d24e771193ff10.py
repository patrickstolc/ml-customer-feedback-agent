import datetime
import pandas_datareader as pdr

# Get the current date
today = datetime.date.today()

# Define the stocks
stocks = {
    'META': 'Meta Platforms, Inc. (META)',
    'TESLA': 'Tesla, Inc. (TSLA)'
}

# Fetch stock data
data = {}
for stock in stocks:
    try:
        info = pdr.get_data_yahoo(f'{stock} US')
        ytd_gain = ((info['Adj Close'][-1] - info['Previous Close'][-1]) / info['Previous Close'][-1]) * 100
        data[stock] = ytd_gain
    except Exception as e:
        print(f'Failed to fetch data for {stock}: {e}')

# Print the date and year-to-date gain
print(f'Today\'s date: {today}')
for stock, gain in data.items():
    if gain is not None:
        print(f'{stock}: {gain:.2f}%')
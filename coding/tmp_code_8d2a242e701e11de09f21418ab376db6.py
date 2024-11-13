import datetime
import yfinance as yf

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
    ticker = yf.Ticker(stock)
    info = ticker.info
    data[stock] = info

# Calculate year-to-date gain
for stock, info in data.items():
    if 'previousClose' in info and 'currentPrice' in info:
        previous_close = info['previousClose']
        current_price = info['currentPrice']
        ytd_gain = ((current_price - previous_close) / previous_close) * 100
        print(f'{stock}: {ytd_gain:.2f}%')
    else:
        print(f'Failed to fetch data for {stock}')

# Print the date
print(f'Today\'s date: {today}')
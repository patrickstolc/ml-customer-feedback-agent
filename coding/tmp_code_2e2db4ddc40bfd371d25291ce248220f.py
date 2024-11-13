import datetime
import yfinance as yf

# Get the current date
today = datetime.date.today()

# Define the stocks
stocks = {
    'META': 'Meta Platforms, Inc. (META)',
    'TSLA': 'Tesla, Inc. (TSLA)'
}

# Fetch stock data for today's date
data = {}
for stock in stocks:
    ticker = yf.Ticker(stock)
    hist = ticker.history(period='1d')
    data[stock] = hist['Close'].iloc[-1]

# Calculate the year-to-date gain
for stock, close_price in data.items():
    if len(data) > 1:
        start_price = data[list(data.keys())[0]]
        ytd_gain = ((close_price - start_price) / start_price) * 100
        print(f'{stock}: {ytd_gain:.2f}%')
    else:
        print(f'No historical data available for {stock}')
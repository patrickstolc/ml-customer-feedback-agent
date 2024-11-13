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
    try:
        info = yf.Ticker(stock)
        info.info
        info.history['2022-01-01':'2024-11-13']
        info.history.index
        info.history.reset_index(inplace=True)
        info.history['Date'] = info.history.index.to_pydatetime().strftime('%Y-%m-%d')
        info.history['Adj Close'] = info.history['Adj Close'].astype(str)
        info.history['Close'] = info.history['Close'].astype(str)
        ytd_gain = ((info.info['currentPrice'] - info.info['previousClose']) / info.info['previousClose']) * 100
        data[stock] = ytd_gain
    except Exception as e:
        print(f'Failed to fetch data for {stock}: {e}')

# Print the date and year-to-date gain
print(f'Today\'s date: {today}')
for stock, gain in data.items():
    if gain is not None:
        print(f'{stock}: {gain:.2f}%')
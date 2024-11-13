import datetime as dt
import yfinance as yf

# Get today's date
today = dt.date.today()
print(f"Today's date is: {today}")

# Define the stock symbols
symbols = ['META', 'TSLA']

# Fetch historical data for each symbol
data = {}
for symbol in symbols:
    ticker = yf.Ticker(symbol)
    # Get the YTD data by slicing from the start of the year to today
    ytd_data = ticker.history(period='1y')
    if not ytd_data.empty:
        data[symbol] = ytd_data['Close'].iloc[-1]
    else:
        print(f"No historical data available for {symbol}")

# Calculate the YTD gain for each stock
gains = {}
for symbol, price in data.items():
    # Assuming we have a hypothetical starting price of $100 for simplicity
    start_price = 100.0
    ytd_gain = (price - start_price) / start_price * 100
    gains[symbol] = ytd_gain

# Print the results
for symbol, gain in gains.items():
    print(f"{symbol} YTD Gain: {gain:.2f}%")
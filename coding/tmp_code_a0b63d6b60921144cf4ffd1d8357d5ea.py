import yfinance as yf

# Define the stock symbols
stock_symbols = ['AAPL', 'GOOGL']

# Loop through each stock symbol and fetch the data
for symbol in stock_symbols:
    # Fetch the stock data for the last 10 days
    stock_data = yf.download(symbol, period='10d')
    
    # Print the stock data
    print(f"Stock Data for {symbol}:")
    print(stock_data)
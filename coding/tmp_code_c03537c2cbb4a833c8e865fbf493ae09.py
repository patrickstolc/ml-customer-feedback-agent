import yfinance as yf

# Define the ticker symbols
ticker_symbols = ["MSFT", "TSLA"]

# Get the current date
current_date = datetime.date.today()

# Fetch historical data for each ticker symbol
for ticker in ticker_symbols:
    data = yf.download(ticker, period="1y")
    if not data.empty:
        # Calculate year-to-date gain
        ytd_gain = (data["Close"][-1] - data["Close"][0]) / data["Close"][0] * 100
        print(f"{ticker}: {ytd_gain:.2f}%")
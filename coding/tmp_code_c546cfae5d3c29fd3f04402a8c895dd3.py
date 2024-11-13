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

# Calculate the year-to-date gain and ROI
for stock, close_price in data.items():
    if len(data) > 1:
        start_price = data[list(data.keys())[0]]
        ytd_gain = ((close_price - start_price) / start_price) * 100
        roi = ((close_price - start_price) / start_price) * 100

        # Calculate additional metrics
        price_volatility = hist['Close'].std() * 252  # Assuming a non-dividend paying stock with 252 trading days per year
        avg_daily_return = (close_price - start_price) / len(hist)
        beta = hist['Close'].covar(yf.Ticker('SP500')) / hist['Close'].var()

        print(f'{stock}:')
        print(f'Year-to-date gain: {ytd_gain:.2f}%')
        if close_price < start_price:
            print('Note: The stock price has decreased significantly.')
        else:
            print('Note: The stock price has increased.')
        print(f'Return on Investment (ROI): {roi:.2f}%')
        print(f'Price Volatility: {price_volatility:.2f}%')
        print(f'Average Daily Return: {avg_daily_return:.2f}%')
        print(f'Beta: {beta:.2f}')
    else:
        print(f'No historical data available for {stock}')
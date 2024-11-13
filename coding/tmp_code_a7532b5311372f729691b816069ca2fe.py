from datetime import date
import yfinance as yf

# Get today's date
today = date.today()
print(f"Today's date: {today}")

# Define stock symbols
symbols = ['META', 'TSLA']

# Loop through each symbol and calculate year-to-date gain
for symbol in symbols:
    # Get the stock data for the current year
    stock_data = yf.download(symbol, start=f'{today.year}-01-01', end=today.strftime('%Y-%m-%d'))
    
    # Calculate the year-to-date gain
    ytd_gain = (stock_data['Close'][-1] - stock_data['Close'][0]) / stock_data['Close'][0]
    
    print(f"Year-to-date gain for {symbol}: {ytd_gain*100:.2f}%")
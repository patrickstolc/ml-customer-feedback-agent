import yfinance as yf

# Define the tickers
tickers = ['META', 'TSLA']

# Get the historical data for each ticker
data = yf.download(tickers, start='2023-01-01')

# Calculate the year-to-date gain
year_to_date_gain_meta = (data['Close'][-1] - data['Close'][0]) / data['Close'][0]
year_to_date_gain_tsla = (data['Close'][-1] - data['Close'][0]) / data['Close'][0]

print(f"Year-to-date gain for META: {year_to_date_gain_meta:.2%}")
print(f"Year-to-date gain for TSLA: {year_to_date_gain_tsla:.2%}")
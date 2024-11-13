import yfinance as yf
from datetime import datetime

# Get today's date
today = datetime.today().strftime('%Y-%m-%d')
print(f"Today's date is: {today}")

# Define the tickers for META and TSLA
tickers = ['META', 'TSLA']

# Fetch historical data for both stocks
data = yf.download(tickers, start='2023-01-01')

# Check if the data was fetched successfully
if data.empty:
    print("Failed to fetch data. Please check your internet connection or try again later.")
else:
    # Calculate YTD gains
    ytd_gain_meta = (data['Close'][-1] - data['Close'][0]) / data['Close'][0]
    ytd_gain_tsla = (data['Close'][-1] - data['Close'][0]) / data['Close'][0]

    print(f"Year-to-date gain for META: {ytd_gain_meta:.2%}")
    print(f"Year-to-date gain for TSLA: {ytd_gain_tsla:.2%}")

    # Compare the YTD gains
    if ytd_gain_meta > ytd_gain_tsla:
        print("META has a higher year-to-date gain.")
    elif ytd_gain_tsla > ytd_gain_meta:
        print("TSLA has a higher year-to-date gain.")
    else:
        print("Both META and TSLA have the same year-to-date gain.")

TERMINATE
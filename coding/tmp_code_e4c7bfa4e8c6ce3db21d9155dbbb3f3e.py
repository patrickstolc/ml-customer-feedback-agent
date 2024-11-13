import datetime
import alpha_vantage

# Get the current date
today = datetime.date.today()

# Define the stocks
stocks = {
    'META': 'Meta Platforms, Inc. (META)',
    'TESLA': 'Tesla, Inc. (TSLA)'
}

# Initialize Alpha Vantage API
av = alpha_vantage.TimesSeriesAPI(key='YOUR_API_KEY')

# Fetch stock data
data = {}
for stock in stocks:
    try:
        info = av.get_daily_adjusted(symbol=stock)
        ytd_gain = ((info['Global Quote']['5. adjusted close'] - info['Global Quote']['4. previous close']) / info['Global Quote']['4. previous close']) * 100
        data[stock] = ytd_gain
    except Exception as e:
        print(f'Failed to fetch data for {stock}: {e}')

# Print the date and year-to-date gain
print(f'Today\'s date: {today}')
for stock, gain in data.items():
    print(f'{stock}: {gain:.2f}%')
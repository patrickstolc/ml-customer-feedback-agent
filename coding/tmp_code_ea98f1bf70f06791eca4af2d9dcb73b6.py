from alpha_vantage.timeseries import TimeSeries

# Initialize the API client
ts = TimeSeries(key='YOUR_API_KEY')

# Fetch historical data for META
data, meta_data = ts.get_daily(symbol='META', outputsize='full')

# Convert the data to a DataFrame
df = pd.DataFrame(data).T

# Set the date as the index
df.set_index('date', inplace=True)

# Calculate the year-to-date gain
year_to_date_gain_meta = (df['4. close'].iloc[-1] - df['4. close'].iloc[0]) / df['4. close'].iloc[0]

print(f"Year-to-date gain for META: {year_to_date_gain_meta:.2%}")
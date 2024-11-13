from datetime import datetime

# Get today's date
today = datetime.now().strftime("%Y-%m-%d")
print(f"Today's date is: {today}")

# Assuming you have access to a financial data source like Yahoo Finance or Alpha Vantage, here's how you might compare the year-to-date gain for META and TSLA:

# For simplicity, let's assume we have a function `get_year_to_date_gain` that returns the gain
def get_year_to_date_gain(symbol):
    # This is a placeholder function. In practice, you would use an API to fetch this data.
    return 10.5  # Example value

# Get year-to-date gains for META and TSLA
meta_gain = get_year_to_date_gain("META")
tsla_gain = get_year_to_date_gain("TSLA")

print(f"Year-to-date gain for META: {meta_gain}%")
print(f"Year-to-date gain for TSLA: {tsla_gain}%")
from datetime import datetime

# Get today's date
today = datetime.now()
print("Today's Date:", today.strftime("%Y-%m-%d"))

# Hypothetical YTD gains (in dollars)
meta_ytd_gain = 1000000  # Example value
tesla_ytd_gain = 500000   # Example value

# Compare the YTD gains
if meta_ytd_gain > tesla_ytd_gain:
    print("META has a higher YTD gain.")
elif meta_ytd_gain < tesla_ytd_gain:
    print("TSLA has a higher YTD gain.")
else:
    print("Both META and TSLA have the same YTD gain.")

# Output today's date
print("Today's Date:", today.strftime("%Y-%m-%d"))
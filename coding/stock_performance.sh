# filename: stock_performance.sh

#!/bin/bash

# Get current date
date=$(date +"%Y-%m-%d")

# Print current date
echo "Today's date is: $date"

# Get historical data for META and TESLA
meta_data=$(curl -s https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&outputsize=full&apikey=YOUR_API_KEY)
tesla_data=$(curl -s https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&outputsize=full&apikey=YOUR_API_KEY)

# Parse data
meta_date=$(echo "$meta_data" | jq -r '.MetaData["Date"]')
tesla_date=$(echo "$tesla_data" | jq -r '.MetaData["Date"]')

# Calculate year-to-date gain for META and TESLA
meta_ytd_gain=$(echo "$meta_data" | jq -r ".TimeSeriesAdjustedClose[\"2024-01-01\"] / .TimeSeriesAdjustedClose[\"2023-01-01\"] - 1")
tesla_ytd_gain=$(echo "$tesla_data" | jq -r ".TimeSeriesAdjustedClose[\"2024-01-01\"] / .TimeSeriesAdjustedClose[\"2023-01-01\"] - 1")

# Print year-to-date gain for META and TESLA
echo "Year-to-date gain for META: $meta_ytd_gain"
echo "Year-to-date gain for TESLA: $tesla_ytd_gain"

# Compare the year-to-date gain for META and TESLA
if (( $(echo "$meta_ytd_gain > $tesla_ytd_gain" | bc -l) )); then
  echo "META has a higher year-to-date gain."
elif (( $(echo "$tesla_ytd_gain > $meta_ytd_gain" | bc -l) )); then
  echo "TESLA has a higher year-to-date gain."
else
  echo "Both META and TESLA have the same year-to-date gain."
fi

# Print current date again for verification
echo "Today's date is: $date"
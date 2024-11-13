curl -o meta_data.csv 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=META&apikey=YOUR_API_KEY'
head -n 5 meta_data.csv
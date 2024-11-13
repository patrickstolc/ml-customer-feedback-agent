# filename: get_stock_prices.py
import requests
import datetime

api_key = "YOUR_API_KEY_HERE"
function = "GLOBAL_QUOTE"
symbol_meta = "META"
symbol_tsla = "TSLA"

url_meta = f"https://www.alphavantage.co/query?function={function}&symbol={symbol_meta}&apikey={api_key}"
url_tsla = f"https://www.alphavantage.co/query?function={function}&symbol={symbol_tsla}&apikey={api_key}"

response_meta = requests.get(url_meta)
response_tsla = requests.get(url_tsla)

data_meta = response_meta.json()
data_tsla = response_tsla.json()

print(f"Current price of META: {data_meta['Global Quote']['05. price']}")
print(f"Current price of TSLA: {data_tsla['Global Quote']['05. price']}")

# Calculate YTD gain
current_date = datetime.date.today()
ytd_start_date = current_date.replace(month=1, day=1)

url_meta_ytd = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_meta}&apikey={api_key}&outputsize=full&datatype=json&fromdate={ytd_start_date.strftime('%Y-%m-%d')}"
response_meta_ytd = requests.get(url_meta_ytd)
data_meta_ytd = response_meta_ytd.json()

url_tsla_ytd = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_tsla}&apikey={api_key}&outputsize=full&datatype=json&fromdate={ytd_start_date.strftime('%Y-%m-%d')}"
response_tsla_ytd = requests.get(url_tsla_ytd)
data_tsla_ytd = response_tsla_ytd.json()

meta_ytd_price = data_meta_ytd['Time Series (Daily)'][list(data_meta_ytd['Time Series (Daily)'].keys())[-1]]['4. close']
tsla_ytd_price = data_tsla_ytd['Time Series (Daily)'][list(data_tsla_ytd['Time Series (Daily)'].keys())[-1]]['4. close']

meta_ytd_gain = ((float(meta_ytd_price) - float(data_meta['Global Quote']['05. price'])) / float(data_meta['Global Quote']['05. price'])) * 100
tsla_ytd_gain = ((float(tsla_ytd_price) - float(data_tsla['Global Quote']['05. price'])) / float(data_tsla['Global Quote']['05. price'])) * 100

print(f"YTD gain of META: {meta_ytd_gain:.2f}%")
print(f"YTD gain of TSLA: {tsla_ytd_gain:.2f}%")
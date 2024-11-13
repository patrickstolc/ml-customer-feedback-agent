# filename: compare_ytd_gain.py
import yfinance as yf
from get_today_date import get_today

meta = yf.Ticker("META")
tsla = yf.Ticker("TSLA")

today = get_today()
start_date = today.replace(year=today.year - 1)
end_date = today

meta_historical = meta.history(start=start_date, end=end_date)
tsla_historical = tsla.history(start=start_date, end=end_date)

meta_ytd_gain = ((meta_historical['Close'].iloc[-1]) / (meta_historical['Close'].iloc[0])) - 1
tsla_ytd_gain = ((tsla_historical['Close'].iloc[-1]) / (tsla_historical['Close'].iloc[0])) - 1

print("META YTD gain:", round(meta_ytd_gain * 100, 2), "%")
print("TSLA YTD gain:", round(tsla_ytd_gain * 100, 2), "%")
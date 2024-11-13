# filename: get_today_date.py
import datetime

def get_today():
    today = datetime.date.today()
    return today

print("Today's date is:", get_today())
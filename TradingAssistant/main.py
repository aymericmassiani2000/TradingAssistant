from scraper import get_all_prices
from emailer import send_email_alert
import json, os

DATA_FILE = "data.json"
ALERT_THRESHOLD = 0.50

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def percent_change(old, new):
    return (new - old) / old if old else 0

def main():
    old_data = load_data()
    new_data = get_all_prices()
    alerts = []

    for source, coins in new_data.items():
        for coin, new_price in coins.items():
            old_price = old_data.get(source, {}).get(coin)
            if old_price:
                change = percent_change(old_price, new_price)
                if abs(change) >= ALERT_THRESHOLD:
                    alerts.append((coin, change, source, new_price))

    if alerts:
        send_email_alert(alerts)

    save_data(new_data)

if __name__ == "__main__":
    main()

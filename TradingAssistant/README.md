# Trading Assistant Bot

Tracks altcoin prices across 5 exchanges and sends an email alert when any coin moves ±50%.

## Exchanges Monitored
- CoinMarketCap
- Uphold
- Kraken
- Binance
- CoinDesk

## Setup

1. Create a `.env` file with:
```
GMAIL_USER=your_email@gmail.com
GMAIL_PASS=your_app_password
```

2. Install dependencies:
```
pip install requests beautifulsoup4
```

3. Run the bot:
```
python main.py
```

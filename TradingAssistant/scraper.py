import requests
from bs4 import BeautifulSoup

def scrape_coinmarketcap():
    url = "https://coinmarketcap.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    coins = {}
    for row in soup.select("tbody tr"):
        name_tag = row.select_one("p.sc-4984dd93-0")
        price_tag = row.select_one("span.sc-7bc56c81-0")
        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.replace("$", "").replace(",", "")
            try:
                coins[name] = float(price)
            except:
                continue
    return coins

def scrape_uphold():
    url = "https://uphold.com/en-us/prices"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    coins = {}
    for div in soup.select("div.asset__row"):
        name_tag = div.select_one("span.asset__title")
        price_tag = div.select_one("span.asset__price")
        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.replace("$", "").replace(",", "")
            try:
                coins[name] = float(price)
            except:
                continue
    return coins

def scrape_kraken():
    url = "https://www.kraken.com/en-gb/prices"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    coins = {}
    for row in soup.select("a.asset-table-row"):
        name_tag = row.select_one("span[data-testid='AssetTableRow-asset-name']")
        price_tag = row.select_one("span[data-testid='AssetTableRow-price']")
        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.replace("$", "").replace(",", "")
            try:
                coins[name] = float(price)
            except:
                continue
    return coins

def scrape_binance():
    url = "https://www.binance.com/en/markets/overview"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    coins = {}
    for row in soup.select("div.css-vlibs4"):
        name_tag = row.select_one("div.css-1ap5wc6")
        price_tag = row.select_one("div.css-ydcgk2")
        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.replace("$", "").replace(",", "")
            try:
                coins[name] = float(price)
            except:
                continue
    return coins

def scrape_coindesk():
    url = "https://www.coindesk.com/price/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    coins = {}
    for div in soup.select("div.price-card"):
        name_tag = div.select_one("div.card-title")
        price_tag = div.select_one("span.price-large")
        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.replace("$", "").replace(",", "")
            try:
                coins[name] = float(price)
            except:
                continue
    return coins

def get_all_prices():
    return {
        "CoinMarketCap": scrape_coinmarketcap(),
        "Uphold": scrape_uphold(),
        "Kraken": scrape_kraken(),
        "Binance": scrape_binance(),
        "CoinDesk": scrape_coindesk()
    }

from pathlib import Path
import csv
import json


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]

def get_first_close(prices):
    return float(prices[0]["close"])

def get_last_close(prices) :
    return float(prices[-1]["close"])

def get_first_date(prices):
    return prices[0]["date"]

def get_last_date(prices):
    return prices[-1]["date"]

def display_market_summary(asset, prices, show_currency=True):

    # Récupérer les informations de l'actif
    ticker = asset["ticker"]
    name = asset["name"]

    # Compter les observations
    observations = len(prices)

    # Récupérer les prix de clôture
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)

    # Récupérer les dates des observations
    first_date = get_first_date(prices)
    last_date = get_last_date(prices)

    # Déterminer si la devise doit être affichée
    if show_currency:
        currency = " " + asset["currency"]
    else:
        currency = ""

    # Afficher les informations
    print(f"{ticker} - {name}")
    print(f"Observations : {observations}")
    print(f"First date   : {first_date}")
    print(f"Last date    : {last_date}")
    print(f"First close : {first_close:.2f}{currency}")
    print(f"Last close  : {last_close:.2f}{currency}")

def main():
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    instrument_latest = instrument_prices[-1]
    benchmark_latest = benchmark_prices[-1]

    display_market_summary(instrument, instrument_prices)
    display_market_summary(benchmark, benchmark_prices, show_currency = False)

    print("=== MarketPulse ===")
    print()
    print("Instrument")
    print(f"{instrument['ticker']} - {instrument['name']}")
    print(f"Last price: {instrument_latest['close']} {instrument['currency']}")
    print()
    print("Benchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    print(f"Last level: {benchmark_latest['close']}")
    print()
    print(f"Period: {LOOKBACK_LABEL}")
    print(f"Interval: {INTERVAL_LABEL}")
    print()
    print("Observations")
    print(f"{instrument['ticker']}: {len(instrument_prices)}")
    print(f"{benchmark['ticker']}: {len(benchmark_prices)}")

if __name__ == "__main__":
    main()
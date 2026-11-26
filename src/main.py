from pathlib import Path
import argparse
import csv
import json

from analytics import (
    align_series,
    calculate_period_return,
    calculate_base_100,
    calculate_relative_performance,
)

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


def get_last_close(prices):
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
    print(f"Market       : {asset['market']}")
    print(f"Observations : {observations}")
    print(f"First date   : {first_date}")
    print(f"Last date    : {last_date}")
    print(f"First close : {first_close:.2f}{currency}")
    print(f"Last close  : {last_close:.2f}{currency}")


def build_market_snapshot(provider_mode="APPROVED_SAMPLE", provider="bloomberg"):
    instruments = load_instruments()
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    if provider == "bloomberg":
        from providers.bloomberg_provider import fetch_bloomberg_prices

        if provider_mode != "APPROVED_SAMPLE":
            raise ValueError("Only APPROVED_SAMPLE is available.")

        instrument_prices = fetch_bloomberg_prices(instrument["ticker"])
        benchmark_prices = fetch_bloomberg_prices(benchmark["ticker"])
        provider_label = "Bloomberg stage - APPROVED_SAMPLE"

    elif provider == "yahoo":
        from providers.yahoo_provider import fetch_yahoo_prices

        instrument_prices = fetch_yahoo_prices(instrument["ticker"])
        benchmark_prices = fetch_yahoo_prices(benchmark["ticker"])
        provider_label = "Yahoo Finance"

    else:
        prices = load_prices()
        instrument_prices = filter_prices(prices, instrument["ticker"])
        benchmark_prices = filter_prices(prices, benchmark["ticker"])
        provider_label = "CSV / JSON"

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices, benchmark_prices
    )

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)

    relative_performance = calculate_relative_performance(
        instrument_return, benchmark_return
    )

    instrument_base_100 = calculate_base_100(aligned_instrument)
    benchmark_base_100 = calculate_base_100(aligned_benchmark)

    return {
        "provider": provider_label,
        "lookback": LOOKBACK_LABEL,
        "interval": INTERVAL_LABEL,
        "instrument": instrument,
        "benchmark": benchmark,
        "instrument_prices": instrument_prices,
        "benchmark_prices": benchmark_prices,
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": relative_performance,
        "instrument_base_100": instrument_base_100,
        "benchmark_base_100": benchmark_base_100,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--provider",
        choices=("csv", "yahoo", "bloomberg"),
        default="bloomberg"
    )
    args = parser.parse_args()

    snapshot = build_market_snapshot(provider=args.provider)

    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]
    instrument_prices = snapshot["instrument_prices"]
    benchmark_prices = snapshot["benchmark_prices"]
    instrument_base_100 = snapshot["instrument_base_100"]
    benchmark_base_100 = snapshot["benchmark_base_100"]

    print("=== MarketPulse ===")
    print()
    print(f"Provider: {snapshot['provider']}")
    print(f"Period: {snapshot['lookback']}")
    print(f"Interval: {snapshot['interval']}")
    print()

    display_market_summary(instrument, instrument_prices)
    print()
    display_market_summary(benchmark, benchmark_prices, show_currency=False)

    print()
    print("Comparison (aligned)")
    print(f"Aligned sessions: {len(instrument_base_100)}")
    print(f"{instrument['ticker']} period return: {snapshot['instrument_return']:+.2f}%")
    print(f"{benchmark['ticker']} period return: {snapshot['benchmark_return']:+.2f}%")
    print(f"Relative performance: {snapshot['relative_performance']:+.2f} percentage points")

    print()
    print("Base 100")
    print(
        f"{instrument['ticker']}: "
        f"{instrument_base_100[0]['value']:.2f} -> "
        f"{instrument_base_100[-1]['value']:.2f}"
    )
    print(
        f"{benchmark['ticker']}: "
        f"{benchmark_base_100[0]['value']:.2f} -> "
        f"{benchmark_base_100[-1]['value']:.2f}"
    )


if __name__ == "__main__":
    main()

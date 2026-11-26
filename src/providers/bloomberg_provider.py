import json


BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}


def load_bloomberg_reference_sample():
    with open("data/sample/bloomberg_reference_sample.json") as file:
        return json.load(file)


def find_reference_series(data, identifier):
    for series in data["series"]:
        if series["provider_identifier"] == identifier:
            return series


def normalize_bloomberg_history(raw_data, canonical_ticker):
    rows = []

    for observation in raw_data["observations"]:
        rows.append({
            "date": observation["observation_date"],
            "ticker": canonical_ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        })

    return rows


def fetch_bloomberg_prices(ticker):
    identifier = BLOOMBERG_IDENTIFIERS[ticker]
    data = load_bloomberg_reference_sample()
    series = find_reference_series(data, identifier)

    return normalize_bloomberg_history(series, series["canonical_ticker"])
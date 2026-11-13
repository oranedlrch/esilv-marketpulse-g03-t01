import yfinance as yf


CANONICAL_TO_YAHOO = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def fetch_yahoo_prices(canonical_ticker, lookback="1mo", interval="1d"):
    symbol = CANONICAL_TO_YAHOO[canonical_ticker]
    data = yf.download(symbol, period=lookback, interval=interval, progress=False)

    if data.empty:
        raise ValueError(f"Yahoo Finance n'a renvoyé aucune donnée pour {symbol}.")

    prices = []
    for date, row in data.sort_index().iterrows():
        prices.append({
            "date": date.strftime("%Y-%m-%d"),
            "ticker": canonical_ticker,
            "open": float(row[("Open", symbol)]),
            "high": float(row[("High", symbol)]),
            "low": float(row[("Low", symbol)]),
            "close": float(row[("Close", symbol)]),
            "volume": int(row[("Volume", symbol)]),
        })

    return prices
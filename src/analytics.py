def index_by_date(prices):
    prices_by_date = {}

    for row in prices:
        prices_by_date[row["date"]] = row

    return prices_by_date


def align_series(instrument_prices, benchmark_prices):
    instrument_by_date = index_by_date(instrument_prices)
    benchmark_by_date = index_by_date(benchmark_prices)
    aligned_instrument=[]
    aligned_benchmark=[]
    for date in sorted(instrument_by_date):
        if date in benchmark_by_date:
            aligned_instrument.append(instrument_by_date[date])
            aligned_benchmark.append(benchmark_by_date[date])
    return aligned_instrument, aligned_benchmark


def calculate_period_return(prices):
    if not prices:
        raise ValueError("The series is empty.")

    first_close = float(prices[0]["close"])
    last_close = float(prices[-1]["close"])

    if first_close == 0:
        raise ValueError("The first close is zero.")

    return ((last_close / first_close) - 1.0) * 100.0


def calculate_base_100(prices):
    if not prices:
        raise ValueError("The series is empty.")
    first_close = float(prices[0]["close"])
    if first_close == 0:
        raise ValueError("The first close is zero.")
    base_100 = []
    for row in prices:
        close = float(row["close"])
        value = (close / first_close) * 100.0
        base_100.append({
            "date": row["date"],
            "ticker": row["ticker"],
            "value": value,
        })
    return base_100

def calculate_relative_performance(instrument_return, benchmark_return):
    return instrument_return - benchmark_return
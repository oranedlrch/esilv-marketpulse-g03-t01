def index_by_date(prices):
    raise NotImplementedError


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
    raise NotImplementedError


def calculate_base_100(prices):
    raise NotImplementedError


def calculate_relative_performance(instrument_return, benchmark_return):
    raise NotImplementedError
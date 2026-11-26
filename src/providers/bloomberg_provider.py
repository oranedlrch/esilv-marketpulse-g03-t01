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
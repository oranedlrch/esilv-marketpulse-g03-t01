# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

Source: `data/sample/bloomberg_reference_sample.json`

Reference: `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md`

Live connectivity: not demonstrated

The sample contains illustrative teaching data, not certified Bloomberg historical observations.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | observation_date | YYYY-MM-DD string |
| ticker | canonical_ticker | AAPL or SP500 |
| open | open_value | Convert to float |
| high | high_value | Convert to float |
| low | low_value | Convert to float |
| close | close_value | Convert to float |
| volume | volume_value | Convert to int |

The source fields are teaching wrapper keys, not Bloomberg LIVE field mnemonics.

Canonical tickers remain AAPL and SP500.

No fields are missing. The benchmark volume is 0 in the approved sample.

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: AAPL US Equity
- Benchmark identifier: SPX Index
- Date representation: YYYY-MM-DD
- Input structure: JSON containing a series list, with an observations list for each asset.
- Missing fields: none.
- Special normalization notes: preserve canonical tickers, convert OHLC values to float and volume to int.

Both series contain 21 observations from 2026-09-01 to 2026-09-30.

Expected canonical reference:

`data/sample/bloomberg_reference_expected.json`
import pandas as pd

def load_nse_stocks():

    url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

    df = pd.read_csv(url)

    stocks = df["SYMBOL"].tolist()

    tickers = [s + ".NS" for s in stocks]

    return tickers[:500]

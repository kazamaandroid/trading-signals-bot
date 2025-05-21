import yfinance as yf
import pandas as pd

def get_ohlcv(symbol, interval="1h", lookback="7d"):
    df = yf.download(tickers=symbol, interval=interval, period=lookback)
    df.dropna(inplace=True)
    return df

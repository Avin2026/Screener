import pandas as pd

def detect_order_block(df):

    last = df.iloc[-3]

    impulse = df.iloc[-1]["Close"] - last["Close"]

    if impulse > df["ATR"].mean():

        return True

    return False


def detect_fvg(df):

    c1 = df.iloc[-3]
    c3 = df.iloc[-1]

    if c1["High"] < c3["Low"]:
        return True

    return False


def detect_liquidity_sweep(df):

    prev_high = df["High"].iloc[-2]
    curr_high = df["High"].iloc[-1]
    close = df["Close"].iloc[-1]

    if curr_high > prev_high and close < prev_high:
        return True

    return False

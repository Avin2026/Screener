import yfinance as yf
import pandas as pd
import json

from smc_engine import *
from stocks_loader import load_nse_stocks

stocks = load_nse_stocks()

results = []

for stock in stocks:

    try:

        df = yf.download(stock, period="6mo", interval="1d")

        if len(df) < 50:
            continue

        df["ATR"] = df["High"] - df["Low"]

        score = 0
        signals = []

        if detect_order_block(df):
            score += 30
            signals.append("Order Block")

        if detect_fvg(df):
            score += 25
            signals.append("Fair Value Gap")

        if detect_liquidity_sweep(df):
            score += 25
            signals.append("Liquidity Sweep")

        volume_spike = df["Volume"].iloc[-1] > df["Volume"].rolling(20).mean().iloc[-1]

        if volume_spike:
            score += 20
            signals.append("Volume Spike")

        if score > 40:

            results.append({
                "stock": stock.replace(".NS",""),
                "price": round(df["Close"].iloc[-1],2),
                "score": score,
                "signals": signals
            })

    except:
        pass

results = sorted(results, key=lambda x: x["score"], reverse=True)

with open("data/setups.json","w") as f:
    json.dump(results,f)

print("Scan completed")

def liquidity_heatmap(df):

    levels = df["High"].round(1)

    counts = levels.value_counts()

    strong_levels = counts[counts > 3]

    return strong_levels.index.tolist()

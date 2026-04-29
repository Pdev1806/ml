import yfinance as yf
import pandas as pd


df = yf.download("GOOGL", start="2024-01-01", end="2025-01-01")

df = df[["Open", "High", "Low", "Close", "Volume"]]
df["Target"] = df["Close"].shift(-1)
df = df.dropna()
print(df.head())

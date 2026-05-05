import pandas as pd
import numpy as np
import yfinance as yf

# -----------------------
# Data
# -----------------------
tickers = ["CL=F", "NG=F", "SPY"]
data = yf.download(tickers, start="2015-01-01")["Close"]
data = data.dropna()

# -----------------------
# Returns
# -----------------------
returns = data.pct_change().dropna()

# -----------------------
# Volatility
# -----------------------
vol_10d = returns.rolling(10).std()
vol_30d = returns.rolling(30).std()

# -----------------------
# Regime Function
# -----------------------
def classify_regime(series):
    low = series.quantile(0.4)
    high = series.quantile(0.8)

    return pd.cut(
        series,
        bins=[-np.inf, low, high, np.inf],
        labels=["Calm", "Normal", "Stress"]
    )

regimes = pd.DataFrame({
    col: classify_regime(vol_10d[col])
    for col in vol_10d.columns
})

# -----------------------
# Shocks
# -----------------------
rolling_vol = returns.rolling(30).std().bfill()
shocks = returns.abs() > (rolling_vol * 2)

# -----------------------
# Output
# -----------------------
output = pd.DataFrame({
    "WTI_Returns": returns["CL=F"],
    "WTI_Vol": vol_10d["CL=F"],
    "NG_Returns": returns["NG=F"],
    "SPY_Returns": returns["SPY"]
})

output.to_csv("cross_asset_volatility_output.csv")

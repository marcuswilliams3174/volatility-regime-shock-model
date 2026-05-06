# Cross-Asset Volatility & Risk Regime Framework (2015–Present)

**Commodities (WTI Crude Oil, Natural Gas) | Equities (S&P 500)**  
**Author: Marcus Williams**  
**Research Focus: Volatility Regimes, Shock Detection, Cross-Asset Risk Transmission**

---

## 🔑 Key Message

This framework analyzes how volatility regimes and shock events evolve across energy commodities and equities, and how cross-asset correlations behave under different market stress conditions.

The model identifies **calm, normal, and stress regimes**, and evaluates how systemic risk propagates during volatility clustering periods.

---

## 📊 Key Insights

- Energy markets (WTI & natural gas) exhibit significantly stronger volatility clustering than equities  
- Natural gas shows the highest frequency of extreme shock events  
- Cross-asset correlations increase during stress periods, reducing diversification benefits  
- Volatility regimes are persistent and structurally clustered rather than random  

---

## 📈 Exhibits

### Exhibit 1 — Cross-Asset Correlation Structure
![Correlation Heatmap](results/correlation_heatmap.png)

Correlation matrix of WTI, natural gas, and S&P 500 returns. Energy assets exhibit stronger co-movement, particularly during stress regimes.

---

### Exhibit 2 — Volatility Regime Distribution (WTI)
![Regime Chart](results/regime_chart.png)

Volatility regimes classified as Calm / Normal / Stress using distribution-based thresholds. Energy markets spend majority time in low-volatility regimes with clustering during macro shocks.

---

### Exhibit 3 — Shock Event Distribution
![Shock Chart](results/shock_chart.png)

Shock events defined as returns exceeding 2× rolling volatility. Natural gas exhibits the highest frequency of extreme moves due to supply-demand sensitivity.

---

## ⚙️ Methodology

- Daily returns computed from Yahoo Finance data (2015–present)
- Rolling volatility (10-day and 30-day standard deviation)
- Regime classification using quantile-based thresholds
- Shock detection using 2× rolling volatility filter
- Cross-asset correlation analysis across regimes

---

## 📌 Interpretation

- Volatility clustering indicates persistent risk regimes rather than random noise  
- During stress periods, correlation convergence reduces diversification effectiveness  
- Energy markets exhibit stronger regime sensitivity due to physical supply constraints  

---

## 🧠 Conclusion

This framework replicates simplified components of institutional risk monitoring systems, including:
- volatility regime detection  
- shock event identification  
- cross-asset correlation breakdown  

It demonstrates how risk propagates across commodities and equities during macro stress periods.

---

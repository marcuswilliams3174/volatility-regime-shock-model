# Cross-Asset Volatility Regime & Shock Detection Model

## Overview
This project builds a simplified cross-asset risk monitoring framework used to identify volatility regimes and shock conditions across commodities and equity markets.

The model analyzes WTI crude oil, natural gas, and S&P 500 data to evaluate how market conditions transition between calm, normal, and stress states, and how asset correlations behave under changing risk regimes.

---

## Objective
The objective of this framework is to replicate simplified components of institutional risk and trading systems by:

- Identifying volatility regimes (calm / normal / stress)
- Detecting shock events relative to rolling volatility thresholds
- Measuring volatility clustering across asset classes
- Evaluating correlation behavior under stress conditions
- Comparing energy markets versus equities during risk-off periods

---

## Data
- WTI Crude Oil Futures (CL=F)
- Natural Gas Futures (NG=F)
- S&P 500 ETF (SPY)
- Source: Yahoo Finance (via yfinance API)
- Frequency: Daily (2015–present)

---

## Methodology

### 1. Return Construction
Daily percentage returns are calculated for all assets.

### 2. Volatility Estimation
Rolling 10-day and 30-day standard deviation is used to capture short-term and medium-term volatility dynamics.

### 3. Regime Classification
Volatility distributions are segmented into three regimes:
- Calm (low volatility conditions)
- Normal (baseline conditions)
- Stress (high volatility periods)

### 4. Shock Detection
Extreme moves are identified when returns exceed 2x rolling volatility.

### 5. Cross-Asset Analysis
Correlation structures are compared across calm vs stress regimes to evaluate how diversification changes under risk-off conditions.

---

## Key Findings

- Energy markets (WTI and natural gas) exhibit stronger volatility clustering than equities.
- Natural gas shows the highest frequency of extreme price shocks.
- Correlation between assets increases during stress periods, indicating reduced diversification benefits.
- Volatility regimes are persistent and exhibit clear clustering behavior rather than random movement.

---

## Interpretation

This framework captures simplified dynamics of real-world trading and risk systems:

- Volatility clustering (persistence of risk)
- Regime switching behavior
- Shock-driven market movements
- Correlation breakdown and convergence during stress

These are core behaviors monitored in commodity trading desks, macro funds, and risk management systems.

---

## Outputs

- Regime classification dataset
- Shock detection signals
- Cross-asset volatility analysis
- Exportable CSV for downstream analysis

---

## Tools Used
Python, Pandas, NumPy, Matplotlib, yFinance

---

## Use Cases

- Commodity trading research
- Energy market volatility analysis
- Macro risk monitoring
- Cross-asset correlation studies

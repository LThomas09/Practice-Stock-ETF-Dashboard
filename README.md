# Practice-Stock-ETF-Dashboard
# Stock/ETF Analysis Dashboard

This project analyzes the risk and return of five major stocks/ETFs over the last five years:

- SPY
- QQQ
- AAPL
- MSFT
- NVDA

## Questions Answered

1. Which stock/ETF performed best?
2. Which was most volatile?
3. What were the worst drawdowns?
4. How correlated were the assets?
5. How did an equal-weight portfolio perform?

## Tools Used

- Python
- pandas
- yfinance
- matplotlib

## Main Findings

NVDA had the highest total return, but it also had the highest volatility and the worst drawdown.  
SPY had lower returns but was more stable.  
QQQ and SPY were highly correlated, meaning they often moved similarly.  
The equal-weight portfolio had strong performance but still carried meaningful risk because of exposure to tech stocks.

## Outputs

The project generates:

- cumulative_returns.png
- drawdowns.png
- portfolio_cumulative_return.png
- stock_analysis_summary.csv

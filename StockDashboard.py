import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
tickers = ["SPY", "QQQ", "AAPL", "MSFT", "NVDA"]

end_date = datetime.today()
start_date = end_date - timedelta(days=5 * 365)

print("Start date:", start_date)
print("End date:", end_date)

price_data = yf.download(tickers, start=start_date, end=end_date)["Close"]

print(price_data.head())

daily_returns = price_data.pct_change()

print("Daily returns:")
print(daily_returns.head())

#Total return over full time period
cumulative_returns = (1 + daily_returns).cumprod() - 1

total_returns = cumulative_returns.iloc[-1]

print("\nTotal returns over the period:")
print(total_returns.sort_values(ascending=False))

# Volatility of each stock
volatility = daily_returns.std() * (252 ** 0.5)

print("\nAnnualized volatility:")
print(volatility.sort_values(ascending=False))

# Worst drawdowns
running_max = price_data.cummax()
drawdowns = (price_data / running_max) - 1
max_drawdowns = drawdowns.min()

print("\nWorst drawdowns (%):")
print((max_drawdowns * 100).sort_values())

# Correlation between daily returns
correlation = daily_returns.corr()

print("\nCorrelation matrix:")
print(correlation)

# Equal-weight portfolio performance
portfolio_returns = daily_returns.mean(axis=1)
portfolio_cumulative_returns = (1 + portfolio_returns).cumprod() - 1

portfolio_total_return = portfolio_cumulative_returns.iloc[-1]
portfolio_volatility = portfolio_returns.std() * (252 ** 0.5)

print("\nEqual-weight portfolio total return (%):")
print(portfolio_total_return * 100)

print("\nEqual-weight portfolio annualized volatility (%):")
print(portfolio_volatility * 100)

# Summary table
summary = pd.DataFrame({
    "Total Return (%)": total_returns * 100,
    "Annualized Volatility (%)": volatility * 100,
    "Worst Drawdown (%)": max_drawdowns * 100
})

summary = summary.sort_values(by="Total Return (%)", ascending=False)

print("\nSummary table:")
print(summary)



# Chart 1: cumulative returns
cumulative_returns.plot(title="Cumulative Returns: Stocks/ETFs")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.savefig("cumulative_returns.png")
plt.close()

# Chart 2: drawdowns
drawdowns.plot(title="Drawdowns: Stocks/ETFs")
plt.xlabel("Date")
plt.ylabel("Drawdown")
plt.savefig("drawdowns.png")
plt.close()

# Chart 3: equal-weight portfolio cumulative return
portfolio_cumulative_returns.plot(title="Equal-Weight Portfolio Cumulative Return")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.savefig("portfolio_cumulative_return.png")
plt.close()

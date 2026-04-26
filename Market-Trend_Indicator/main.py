import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2023-01-01", end="2024-01-01")


# 21-day SMA
data['SMA_21'] = data['Close'].rolling(window=21).mean()

# EMAs
data['EMA_8'] = data['Close'].ewm(span=8, adjust=False).mean()
data['EMA_21'] = data['Close'].ewm(span=21, adjust=False).mean()
data.columns = data.columns.get_level_values(0)

def get_signal(row):
    price_above_sma = row['Close'] > row['SMA_21']
    ema_bull = row['EMA_8'] > row['EMA_21']

    if price_above_sma and ema_bull:
        return "Strong Bull"
    elif price_above_sma and not ema_bull:
        return "Weak Bull"
    elif not price_above_sma and ema_bull:
        return "Recovery"
    else:
        return "Bear"

data['Signal'] = data.apply(get_signal, axis=1)
latest_signal = data['Signal'].iloc[-1]

plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Price')
plt.plot(data['SMA_21'], label='21 SMA')
plt.plot(data['EMA_8'], label='EMA 8')
plt.plot(data['EMA_21'], label='EMA 21')

plt.title(f"Market Trend Indicator - {latest_signal}")
plt.legend()
plt.show()

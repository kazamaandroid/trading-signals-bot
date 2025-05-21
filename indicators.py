import ta

def apply_indicators(df):
    df["ema_fast"] = ta.trend.ema_indicator(df["Close"], window=9).ema_indicator()
    df["ema_slow"] = ta.trend.ema_indicator(df["Close"], window=21).ema_indicator()
    df["rsi"] = ta.momentum.rsi(df["Close"])
    return df

def check_signals(df):
    signals = []
    if df["ema_fast"].iloc[-2] < df["ema_slow"].iloc[-2] and df["ema_fast"].iloc[-1] > df["ema_slow"].iloc[-1]:
        signals.append("Cruce alcista EMA")
    if df["rsi"].iloc[-1] > 70:
        signals.append("RSI sobrecomprado")
    if df["rsi"].iloc[-1] < 30:
        signals.append("RSI sobrevendido")
    return signals

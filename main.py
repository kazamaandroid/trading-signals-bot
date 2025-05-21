from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, SYMBOLS, TIMEFRAMES
from fetch_data import get_ohlcv
from indicators import apply_indicators, check_signals
from plot_chart import plot_price

bot = Bot(token=TELEGRAM_BOT_TOKEN)

for symbol in SYMBOLS:
    df = get_ohlcv(symbol, interval="1h")
    df = apply_indicators(df)
    signals = check_signals(df)

    if signals:
        msg = f"Señales detectadas para {symbol}:\n" + "\n".join(f"- {s}" for s in signals)
        chart = plot_price(df, symbol)
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=chart, caption=msg)

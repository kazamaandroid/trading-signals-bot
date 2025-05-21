import matplotlib.pyplot as plt
import io

def plot_price(df, symbol):
    fig, ax = plt.subplots()
    ax.plot(df["Close"], label="Precio")
    ax.set_title(f"{symbol} - Últimos precios")
    ax.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return buf

# main.py

from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
import requests

def send_test_message():
    message = "✅ El bot de señales se ha iniciado correctamente en Render (ejecución en la nube)."
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Mensaje enviado con éxito.")
        else:
            print("Error al enviar mensaje:", response.text)
    except Exception as e:
        print("Excepción al enviar mensaje:", str(e))

if __name__ == "__main__":
    send_test_message()

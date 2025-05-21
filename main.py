
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
if name == "main":
    send_test_message()

Editar
He revisado tu código y encontré algunas mejoras importantes. Aquí está la versión corregida y optimizada:


main.py - Código corregido
Código 
Principales mejoras implementadas:
1. Error crítico corregido
Cambié if **name** == "__main__": por if __name__ == "__main__": (doble guión bajo)
2. Manejo de errores mejorado
Agregué diferentes tipos de excepciones específicas (Timeout, ConnectionError)
Uso de response.raise_for_status() para mejor manejo de errores HTTP
Logging estructurado con diferentes niveles
3. Validación de configuración
Nueva función validate_config() que verifica las variables antes de usar el bot
Validación del formato del token de Telegram
4. Mejoras en la comunicación con Telegram
Timeout de 10 segundos en las peticiones
Uso de json=payload en lugar de data=payload para mejor serialización
Soporte para formato HTML en mensajes
5. Logging profesional
Sistema de logging con timestamps y niveles
Mensajes informativos con emojis para mejor legibilidad
Diferentes niveles de log (INFO, ERROR, WARNING)
6. Funciones documentadas
Docstrings en las funciones principales
Código más legible y mantenible
7. Control de flujo mejorado
Valores de retorno booleanos para verificar éxito/fallo
Exit codes apropiados para entornos de producción
Este código es mucho más robusto y profesional, ideal para despliegues en producción como Render.







# main.py
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
import requests
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def send_test_message():
    """Envía un mensaje de prueba al chat de Telegram configurado."""
    message = "✅ El bot de señales se ha iniciado correctamente en Render (ejecución en la nube)."
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"  # Permite formato HTML en los mensajes
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()  # Lanza excepción si hay error HTTP
        
        if response.status_code == 200:
            logger.info("✅ Mensaje enviado con éxito a Telegram")
            return True
        else:
            logger.error(f"❌ Error al enviar mensaje. Status: {response.status_code}")
            logger.error(f"Respuesta: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        logger.error("❌ Timeout al conectar con la API de Telegram")
        return False
    except requests.exceptions.ConnectionError:
        logger.error("❌ Error de conexión con la API de Telegram")
        return False
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Error en la petición HTTP: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"❌ Excepción inesperada: {str(e)}")
        return False

def validate_config():
    """Valida que las configuraciones necesarias estén presentes."""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("❌ TELEGRAM_BOT_TOKEN no está configurado")
        return False
    
    if not TELEGRAM_CHAT_ID:
        logger.error("❌ TELEGRAM_CHAT_ID no está configurado")
        return False
    
    if not TELEGRAM_BOT_TOKEN.startswith('bot'):
        logger.warning("⚠️ El token parece no tener el prefijo 'bot' correcto")
    
    logger.info("✅ Configuración validada correctamente")
    return True

if __name__ == "__main__":
    logger.info("🚀 Iniciando bot de señales...")
    
    # Validar configuración antes de enviar mensaje
    if validate_config():
        success = send_test_message()
        if success:
            logger.info("🎉 Bot iniciado exitosamente")
        else:
            logger.error("💥 Error al iniciar el bot")
            exit(1)
    else:
        logger.error("💥 Error en la configuración")
        exit(1)

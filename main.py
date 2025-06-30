import os
import time
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Message sent")
        else:
            print("❌ Failed to send message")
    except Exception as e:
        print("Error:", e)

# Example signal logic (to replace with real analysis later)
def run_bot():
    while True:
        signal = "📊 Signal XAUUSD détecté (exemple test)"
        send_message(signal)
        time.sleep(300)  # Send every 5 minutes

if __name__ == "__main__":
    send_message("🤖 Bot IA XAUUSD activé sur Railway")
    run_bot()

import os
import requests

token = os.environ["BOT_TOKEN"]
chat_id = os.environ["CHAT_ID"]

text = "Привіт! Це щоденне повідомлення 🙂"

url = f"https://api.telegram.org/bot{token}/sendMessage"
r = requests.post(url, data={"chat_id": chat_id, "text": text})
r.raise_for_status()
print("Sent OK")

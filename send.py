import os
import requests

token = os.environ["BOT_TOKEN"]
chat_id = os.environ["CHAT_ID"]
text = "Тестове повідомлення"

url = f"https://api.telegram.org/bot{token}/sendMessage"
r = requests.post(url, data={"chat_id": chat_id, "text": text})

print("STATUS:", r.status_code)
print("RESPONSE:", r.text)  # <-- це найважливіше

r.raise_for_status()
print("Sent OK")

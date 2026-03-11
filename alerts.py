import requests

def telegram_alert(message):

    token = "BOT_TOKEN"
    chat = "CHAT_ID"

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    requests.post(url, data={"chat_id":chat,"text":message})

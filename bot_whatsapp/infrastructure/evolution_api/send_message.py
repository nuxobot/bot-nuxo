import os
import requests

def send_message(number: str, message: str) -> dict:
    url = "http://localhost:8081/message/sendText/celular"

    payload = {
        "number": number,
        "text": message
    }
    headers = {
        "apikey": os.getenv("AUTHENTICATION_API_KEY"),
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()
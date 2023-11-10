import json
import requests
from src import settings
import os

def app_initialized():
    if not os.path.is_dir("data"):
        os.mkdir("data")

    if os.path.exists("data/credentials.json"):
        with open("data/credentials.json", "r") as file:
            return json.load(file), True
    return None, False

def remove_token():
    if not settings.USERNAME:
        return
    url = "https://bydtvrscl5.execute-api.ap-southeast-1.amazonaws.com/remove_token?token=mKJDlkjsdioJMD809sdm89DUM98sdkmKLDJ"
    payload = {
        "username": settings.USERNAME,
        "password": settings.PASSWORD,
        "token": settings.TOKEN
    }
    response = requests.post(url=url, json=payload)
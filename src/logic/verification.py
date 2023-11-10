import json
import requests
from pprint import pprint
from src import settings

def verify_credentials(login_screen):
    username = login_screen.username.get()
    password = login_screen.password.get()
    stay_logged_in = login_screen.stay_logged_in.get()

    authentication_endpoint = f"https://bydtvrscl5.execute-api.ap-southeast-1.amazonaws.com/authenticate_user?token=mKJDlkjsdioJMD809sdm89DUM98sdkmKLDJ"
    json_body = {
        "username": username,
        "password": password
    }
    response_body = json.loads(requests.post(url=authentication_endpoint, json=json_body).text)
    authorized = response_body.get("authorized")
    if not authorized:
        pprint(response_body)
        login_screen.error_message.set(response_body["message"])
        return

    settings.USERNAME = username
    settings.PASSWORD = password
    settings.STAY = stay_logged_in
    settings.TOKEN = response_body["token"]

    if stay_logged_in:
        with open("data/credentials.json", "w") as file:
            json.dump({"username": username, "password": password}, file)
    
    change_screen(login_screen)


def change_screen(login_screen):
    login_screen.pack_forget()
    login_screen.parent_window.email_sender.pack()

from src import settings
import requests
import csv
import time

def submit(email_sender):
    subject = email_sender.subject.get()
    template_path = email_sender.template.get()
    data_path = email_sender.data.get()
    message = email_sender.message
    message.set("")

    # Create template
    endpoint = f"https://bydtvrscl5.execute-api.ap-southeast-1.amazonaws.com/create_template?username={settings.USERNAME}&token={settings.TOKEN}"
    with open(template_path) as file:
        html_content = file.read()
    json={
        "template_name": subject.replace(" ", "-"),
        "subject": subject,
        "html_content": html_content
    }
    response = requests.post(url=endpoint, json=json)

    # Send emails
    endpoint = f"https://bydtvrscl5.execute-api.ap-southeast-1.amazonaws.com/send_email?username={settings.USERNAME}&token={settings.TOKEN}"
    with open(data_path, encoding="latin-1") as file:
        contents = list(csv.DictReader(file, delimiter=","))
    for data in contents:
        print(f"Processing {data['NICKNAME']}...")
        json = {
            "template_name": subject.replace(" ", "-"),
            "template_data": data,
            "username": settings.USERNAME,
            "recipient": data["EMAIL"]
        }
        requests.post(url=endpoint, json=json)
        print(f"{data['NICKNAME']} done!")
        time.sleep(0.1)

    # Delete template
    endpoint = f"https://bydtvrscl5.execute-api.ap-southeast-1.amazonaws.com/delete_template?username={settings.USERNAME}&token={settings.TOKEN}"
    json = {
        "template_name": subject.replace(" ", "-")
    }
    requests.delete(url=endpoint, json=json)
    message.set("Done!")

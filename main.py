import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "egemenito"
TOKEN = "YOUR TOKEN"
DATE = datetime.date.today()
FORMATTED_DATE = DATE.strftime("%Y%m%d")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params={
    "id": "graph1",
    "name": "Habit Tracker",
    "unit": "Pages read",
    "type": "int",
    "color": "shibafu",
}

pixelpost_endpoint = f"{graph_endpoint}/graph1"

pixel_params={
    "date": FORMATTED_DATE,
    "quantity": "35"
}
pixelpost_response = requests.post(url=pixelpost_endpoint, json=pixel_params, headers=headers)
print(pixelpost_response.text)

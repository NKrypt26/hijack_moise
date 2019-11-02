import requests
import json
import numpy as np

response = requests.get("http://api.open-notify.org/astros.json")
#print(response.status_code)
todos = json.loads(response.text)

people = todos["people"]

for person in people:
    print(person["name"])



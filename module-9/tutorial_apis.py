#Rashai Robertson
#CSD_325
#4/27/2025
#Module 9.2

import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)


import json

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
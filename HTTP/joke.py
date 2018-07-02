#Program that retrieve json format data and covert it into dictionary
#Print the joke when program is run

import requests

url = "https://www.icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept": "application/json"})

data=response.json()
print(data["joke"])
print("The status code  is {} ".format(response.status_code))
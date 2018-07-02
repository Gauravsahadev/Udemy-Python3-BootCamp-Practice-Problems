# Program to send request to site and retrieve data from the sites

import requests

url = "https://www.icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept": "text/plain"})
print(response.text)

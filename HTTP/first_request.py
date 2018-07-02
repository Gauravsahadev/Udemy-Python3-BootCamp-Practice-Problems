# A simple http get request to www.facebook.com


import requests

url = "https://www.facebook.com"
response = requests.get(url)

print("you requests for {} with status code {} ".format(url, response.status_code))
#print("\n", response.text)

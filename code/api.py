import requests
url = "https://swapi.dev/api/planets/19"
resp = requests.get(url)
data = resp.json()

print(data)

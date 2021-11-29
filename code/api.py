import requests
url = "https://swapi.dev/api/planets"
resp = requests.get(url)
data = resp.json()
plan_num = input("enter a planet number: ")
show_plan = url, '/', str(plan_num)
print(data)

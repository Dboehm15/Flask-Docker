import requests
import json
# TODO come up with a way to not just have the authorization information sitting in the repo
url = "https://oauth.battle.net/token"

payload = 'grant_type=client_credentials'
headers = {
    'Authorization': 'Basic MWMxYmI4YjJiOWQ1NDVlZjk5MzUxNmQ1MGJmYjNmZDY6b21sc1A0bG1nOVA2NlNaYTNyM2VueUp2QVVqcGZmeVQ=',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

data = response.json()

with open("data.json", "w") as f:
    json.dump(data, f)

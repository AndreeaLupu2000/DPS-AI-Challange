import requests

url = "https://dps-ai-challenge-andreea-2341b9cca97c.herokuapp.com/predict"

data = {
    'year': 2021,
    'month': 1
}

response = requests.post(url, json=data)
print(response.json())

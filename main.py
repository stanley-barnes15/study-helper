import requests

url = 'https://opentdb.com/api.php?amount=1'
response = requests.get(url)
data = response.json()
print(data)
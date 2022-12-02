from requests import requests
import json

#1
url = ''
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)
print(response.text)

#2
res = requests.get('https://')
response = json.loads(res.text)

#3
url = 'web address'
params = {'key': 'value'}
r = requests.get(url=URL, params=PARAMS)
response = r.json()

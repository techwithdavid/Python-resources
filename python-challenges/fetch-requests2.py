import requests
import json

#Connect to API
response_API = requests.get(
    'https://api.covid19india.org/state_district_wise.json')
#print(response_API.status_code)
#GET API data
data = response_API.text
#Parse data into JSON format
json.loads(data)
#Extract data and print it
parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']

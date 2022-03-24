import requests
import json

def clean_data():
    r = requests.get('https://brealy-padron-portfolio-react.vercel.app/')
    return r.json()

results = clean_data()

for key, values in list(results.items()):
    if isinstance(values, list):
        for item in values:
            if item in ['', 'N/A', '-']:
                values.remove(item)
    elif isinstance(values, dict):
        for inner_key, inner_value in list(values.items()):
            if item in ['', 'N/A', '-']:
                del values[inner_key]
    elif values in ['', 'N/A', '-']:
        del results[key]

print(json.dumps(results))
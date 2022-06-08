import requests
import pandas as pd


API_KEY = API_KEY


url = 'https://api.pagerduty.com/incidents?limit=50'
headers = {
    'Accept': 'application/vnd.pagerduty+json;version=2',
    'Authorization': 'Token token={token}'.format(token=API_KEY)}
r = requests.get(url, headers=headers)
data = r.content
data_dict = json.loads(data)
data_df = pd.DataFrame(data_dict['incidents'])

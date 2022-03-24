import requests

r = requests.get("http://neighbordevcr.com")       
print(r.status_code)
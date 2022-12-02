import requests

BASE_URL = 'https://fakestoreapi.com'


response = requests.delete(f"{BASE_URL}/products/21")
print(response.json())

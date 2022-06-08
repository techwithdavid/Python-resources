import requests

BASE_URL = 'https://fakestoreapi.com'

response = requests.get(f"{BASE_URL}/products")
print(response.json())

query_params = {
    "limit": 3
}

response2 = requests.get(f"{BASE_URL}/products", params=query_params)
print(response2.json())

response3 = requests.get(f"{BASE_URL}/products/18")
print(response3)

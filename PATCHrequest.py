import requests

BASE_URL = 'https://fakestoreapi.com'

updated_product = {
    "category": 'electronic'
}

response = requests.patch(f"{BASE_URL}/products/21", json=updated_product)
print(response.json())

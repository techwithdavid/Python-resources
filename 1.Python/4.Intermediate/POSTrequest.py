import json
import requests

BASE_URL = 'https://fakestoreapi.com'

new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

response = requests.post(f"{BASE_URL}/products", json=new_product)
print(response.json())

headers = {
    "Content-Type": "application/json"
}

response2 = requests.post(f"{BASE_URL}/products",
                         data=json.dumps(new_product), headers=headers)
print(response2.json())

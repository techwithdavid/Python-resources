import requests

result = requests.get('https:/')

resp_data = result.json()["data"].split(",")

count = 0
for data in resp_data:
    split_data = data.split("=")
    if split_data[0].strip() == "age" and int(split_data[1]) >= 50:
        count += 1

print(count)




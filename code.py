import requests
import json
import csv

url = 'https://api.thecatapi.com/v1/images/search'

response = requests.get(url)

if response.status_code == 200:
    cat_data = response.json()

    # store as json format 
    with open('cats_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(cat_data, json_file, ensure_ascii=False, indent=4)

else:
    print(f"failed：{response.status_code}")

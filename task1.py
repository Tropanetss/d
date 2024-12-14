import json
import requests
from requests import exceptions

API_URL = "https://dummyjson.com/products"
OUTPUT_FILE ="products.json"

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except exceptions.RequestException as e:
        print(e)
        return None

def save_to_file(data, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=True, indent=4)

        print(filename)

    except IOError as e:
        print("Error while saving")

data = fetch_data(API_URL)
print(data)
save_to_file(data, OUTPUT_FILE)
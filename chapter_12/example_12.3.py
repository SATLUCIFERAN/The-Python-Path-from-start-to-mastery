
import requests

url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "Authorization": "Bearer YOUR_REAL_API_TOKEN",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    payload = response.json()
    print("Fetched posts successfully. Number of items:", len(payload))
else:
    print("Error:", response.status_code, response.text)

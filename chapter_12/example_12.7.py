
import requests

url = "https://jsonplaceholder.typicode.com/invalid-endpoint"
r = requests.get(url)

# 1) Quick boolean check
if r.ok:
    data = r.json()
else:
    print("Failed! Status code:", r.status_code)

# 2) Raise an exception for 4xx/5xx automatically
try:
    r.raise_for_status()             # raises HTTPError if status is 4xx/5xx
    data = r.json()
except requests.exceptions.HTTPError as err:
    print("HTTP error occurred:", err)
except ValueError:
    print("Response wasn't valid JSON.")

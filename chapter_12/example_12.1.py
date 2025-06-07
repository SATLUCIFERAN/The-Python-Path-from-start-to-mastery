
import requests

# 1. Define the endpoint URL
url = "https://jsonplaceholder.typicode.com/posts"

# 2. Send a GET request
response = requests.get(url)

# 3. Check the HTTP status code
print(response.status_code)  # 200 indicates success

# 4. Inspect headers if needed
print(response.headers.get("Content-Type"))
# → e.g., "application/json; charset=utf-8"

# 5. Get the raw text (string) of the response
print(response.text[:200])  # print first 200 characters

# 6. Parse the JSON body (if Content-Type is JSON)
data = response.json()  # returns a Python list or dict
print(type(data))       # <class 'list'>


'''
 {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita
<class 'list'>

'''
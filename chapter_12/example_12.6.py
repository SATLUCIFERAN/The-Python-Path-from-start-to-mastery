
import requests

user_response = requests.get("https://jsonplaceholder.typicode.com/users/1")
user_payload = user_response.json()
print(user_payload["name"])           # Leanne Graham
print(user_payload["email"])          # Sincere@april.biz
print(user_payload["address"]["city"]) # Gwenborough

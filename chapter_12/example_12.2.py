
import requests

base_url = "https://jsonplaceholder.typicode.com/comments"

# Suppose we only want comments for postId=3
params = {
    "postId": 3
}

resp = requests.get(base_url, params=params)
print(resp.status_code)
print(resp.url)

comments = resp.json()
print(len(comments))
print(comments[0])

'''
00
https://jsonplaceholder.typicode.com/comments?postId=3
5
{'postId': 3, 'id': 11, 'name': 'fugit labore quia mollitia quas deserunt nostrum sunt', 
'email': 'Veronica_Goodwin@timmothy.net', 
'body': 'ut dolorum nostrum id quia aut est\nfuga est inventore vel 
eligendi explicabo quis consectetur\naut occaecati repellat id natus quo est\n
ut blanditiis quia ut vel ut maiores ea'}

'''
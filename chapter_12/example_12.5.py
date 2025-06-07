import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()          # data is now a Python list of dicts
    print(type(data))               # <class 'list'>
    first_item = data[0]            # each item is a dict
    print(type(first_item))         # <class 'dict'>
    print(first_item.keys())        # dict_keys(['userId', 'id', 'title', 'body'])
else:
    print("Request failed:", response.status_code)

for post in data[:3]:  # just show the first three posts
    print(f"Post ID: {post['id']}")
    print(f"Title   : {post['title']}")
    print("---")


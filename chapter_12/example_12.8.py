
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
content_type = resp.headers.get("Content-Type", "")

if "application/json" in content_type:
    try:
        payload = resp.json()
        print(payload)
        # … work with JSON …
    except ValueError:
        print("Invalid JSON received.")
else:
    # Not JSON: maybe an error page or plaintext
    print("Unexpected content type:", content_type)
    print("Raw response text (first 300 chars):")
    print(resp.text[:300])

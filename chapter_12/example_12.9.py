
import requests

def fetch_comments_for_post(post_id):
    """
    Example function: calls JSONPlaceholder to fetch comments for a given post_id.
    """
    base_url = "https://jsonplaceholder.typicode.com/comments"
    params = {
        "postId": post_id
    }
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error on 4xx/5xx
    except requests.exceptions.RequestException as e:
        print(f"Error contacting JSONPlaceholder API: {e}")
        return

    content_type = response.headers.get("Content-Type", "")
    if "application/json" not in content_type:
        print(f"Unexpected content type: {content_type}")
        print("Response text (first 200 chars):", response.text[:200])
        return

    try:
        data = response.json()
    except ValueError:
        print("Received invalid JSON.")
        return

    # Now `data` is a list of comment-dicts
    print(f"Comments for post ID {post_id}:")
    for comment in data[:5]:  # show the first 5 comments
        print(f" • {comment['name']} ({comment['email']}): {comment['body'][:50]}…")

if __name__ == "__main__":
    fetch_comments_for_post(1)

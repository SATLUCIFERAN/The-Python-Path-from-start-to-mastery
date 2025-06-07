import requests
import pandas as pd
import datetime
import yaml
import os

# ──────────────────────────────────────────────────────────────────────────────
#  Load config.yaml
# ──────────────────────────────────────────────────────────────────────────────
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# ──────────────────────────────────────────────────────────────────────────────
#  Diagnose what’s in data_folder (debugging stray CR/LF issues)
# ──────────────────────────────────────────────────────────────────────────────
raw_data_folder = config.get("data_folder", "")
print("Raw data_folder repr:", repr(raw_data_folder))

# Show each character + its Unicode codepoint
chars = list(raw_data_folder)
codepoints = [hex(ord(ch)) for ch in raw_data_folder]
print("  → Individual characters:", chars)
print("  → Unicode codepoints:", codepoints)
# Example output if there was a hidden CR: ['d','a','t','a','\r'] and ['0x64','0x61','0x74','0x61','0xd']

# ──────────────────────────────────────────────────────────────────────────────
#  Strip out hidden chars, then strip whitespace
# ──────────────────────────────────────────────────────────────────────────────
for bad in ["\r", "\n", "\ufeff", "\u200b", "\u200c", "\u200d"]:
    raw_data_folder = raw_data_folder.replace(bad, "")
data_folder = raw_data_folder.strip()
print("Clean data_folder repr:", repr(data_folder))  # Should now be exactly 'data'

# Repeat for report_folder
raw_report_folder = config.get("report_folder", "")
for bad in ["\r", "\n", "\ufeff", "\u200b", "\u200c", "\u200d"]:
    raw_report_folder = raw_report_folder.replace(bad, "")
report_folder = raw_report_folder.strip()
print("Clean report_folder repr:", repr(report_folder))

# ──────────────────────────────────────────────────────────────────────────────
#  Build the Reddit JSON endpoint URL
# ──────────────────────────────────────────────────────────────────────────────
subreddit = config["subreddit"]  # e.g. "r/programming"
limit     = config["limit"]      # e.g. 20
url = f"https://www.reddit.com/{subreddit}/top/.json?limit={limit}&t=day"

# Custom User-Agent—Reddit requires this to avoid generic “python-requests” blocks
headers = {
    "User-Agent": "python:reddit_top_report:v1.0 (by /u/your_reddit_username)"
}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Error fetching data: HTTP {response.status_code}")
    exit(1)
data = response.json()

# ──────────────────────────────────────────────────────────────────────────────
#  Extract fields into a Pandas DataFrame
# ──────────────────────────────────────────────────────────────────────────────
records = []
for idx, child in enumerate(data["data"]["children"], start=1):
    post = child["data"]
    records.append({
        "rank": idx,
        "title": post["title"],
        "url": post["url"],
        "score": post["score"],
        "author": post["author"],
        "comments": post["num_comments"],
        # Convert UNIX timestamp to Python datetime (in local timezone)
        "created_utc": datetime.datetime.fromtimestamp(post["created_utc"]),
        # Build a clickable Reddit link
        "permalink": "https://reddit.com" + post["permalink"]
    })

df = pd.DataFrame(records)

# ──────────────────────────────────────────────────────────────────────────────
#  Ensure data_folder exists
# ──────────────────────────────────────────────────────────────────────────────
os.makedirs(data_folder, exist_ok=True)

# ──────────────────────────────────────────────────────────────────────────────
# Save timestamped CSV
# ──────────────────────────────────────────────────────────────────────────────
today_str = datetime.datetime.now().strftime("%Y-%m-%d")

# Important: Replace "/" with "_" so Windows doesn’t treat “r/programming” as a path.
safe_subreddit = subreddit.replace("/", "_")  # becomes "r_programming"
csv_filename = f"{safe_subreddit}_top_{today_str}.csv"
csv_path = os.path.join(data_folder, csv_filename)

try:
    df.to_csv(csv_path, index=False)
    print(f"Saved top posts to {csv_path}")
except OSError as e:
    print(f"Failed to save CSV: {e}")
    exit(1)

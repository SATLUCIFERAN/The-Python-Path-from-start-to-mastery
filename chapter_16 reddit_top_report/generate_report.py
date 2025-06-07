import pandas as pd
import datetime
import yaml
import os
from jinja2 import Environment, FileSystemLoader

# ──────────────────────────────────────────────────────────────────────────────
# Load config.yaml
# ──────────────────────────────────────────────────────────────────────────────
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# ──────────────────────────────────────────────────────────────────────────────
# Clean & ensure report_folder exists
# ──────────────────────────────────────────────────────────────────────────────
raw_report_folder = config.get("report_folder", "")
for bad in ["\r", "\n", "\ufeff", "\u200b", "\u200c", "\u200d"]:
    raw_report_folder = raw_report_folder.replace(bad, "")
report_folder = raw_report_folder.strip()
os.makedirs(report_folder, exist_ok=True)

# ──────────────────────────────────────────────────────────────────────────────
# Clean & locate data_folder
# ──────────────────────────────────────────────────────────────────────────────
raw_data_folder = config.get("data_folder", "")
for bad in ["\r", "\n", "\ufeff", "\u200b", "\u200c", "\u200d"]:
    raw_data_folder = raw_data_folder.replace(bad, "")
data_folder = raw_data_folder.strip()

# List all CSV files in data_folder (case-insensitive ".csv" extension)
all_csv = [f for f in os.listdir(data_folder) if f.lower().endswith(".csv")]
if not all_csv:
    print(f"No CSV files found in {data_folder}")
    exit(1)

# Sort lexicographically so “YYYY-MM-DD” newest is last
all_csv.sort()
latest_csv = all_csv[-1]
csv_path = os.path.join(data_folder, latest_csv)
print("Using CSV:", csv_path)

# ──────────────────────────────────────────────────────────────────────────────
# Read CSV into DataFrame
# ──────────────────────────────────────────────────────────────────────────────
df = pd.read_csv(csv_path)

# If "created_utc" is already a string or ISO date in the CSV, we re-format it:
df["created_utc_str"] = pd.to_datetime(df["created_utc"], errors="coerce") \
                         .dt.strftime("%Y-%m-%d %H:%M:%S")

# ──────────────────────────────────────────────────────────────────────────────
# Prepare data for Jinja (list of dicts)
# ──────────────────────────────────────────────────────────────────────────────
posts = df.to_dict(orient="records")

# ──────────────────────────────────────────────────────────────────────────────
# Set up Jinja2 environment & load template
# ──────────────────────────────────────────────────────────────────────────────
env = Environment(loader=FileSystemLoader("templates"))
template_path = os.path.basename(config["html_template"])
template = env.get_template(template_path)

# ──────────────────────────────────────────────────────────────────────────────
# Build context for template
# ──────────────────────────────────────────────────────────────────────────────
today_str = datetime.datetime.now().strftime("%Y-%m-%d")
context = {
    "subreddit": config["subreddit"],
    "limit": config["limit"],
    "date": today_str,
    "posts": posts,
}

# ──────────────────────────────────────────────────────────────────────────────
# Render HTML
# ──────────────────────────────────────────────────────────────────────────────
rendered_html = template.render(context)

# ──────────────────────────────────────────────────────────────────────────────
# Save rendered HTML to report_folder
# ──────────────────────────────────────────────────────────────────────────────
safe_subreddit = config["subreddit"].replace("/", "_")
html_filename = f"{safe_subreddit}_top_{today_str}.html"
html_path = os.path.join(report_folder, html_filename)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("Saved HTML report to", html_path)







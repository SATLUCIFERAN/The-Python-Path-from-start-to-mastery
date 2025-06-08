import os
import datetime
import yaml
import keyring
import re
from yagmail import SMTP
from jinja2 import Template

def load_config():
    with open("config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def find_latest_report(report_folder, safe_subreddit):
    candidates = [
        fname for fname in os.listdir(report_folder)
        if fname.startswith(safe_subreddit + "_top_") and fname.lower().endswith(".html")
    ]
    if not candidates:
        return None
    candidates.sort()
    return os.path.join(report_folder, candidates[-1])

def render_subject(template_str, context):
    return Template(template_str).render(context)

def main():
    cfg = load_config()

    # If email is disabled, just exit
    if not cfg.get("email", {}).get("enabled", False):
        print("Email sending is disabled in config.yaml. Exiting.")
        return

    # ──────────────────────────────────────────────────────────────────────────
    # Clean & identify report_folder
    # ──────────────────────────────────────────────────────────────────────────
    raw_report = cfg.get("report_folder", "")
    for ch in ["\r", "\n", "\ufeff", "\u200b", "\u200c", "\u200d"]:
        raw_report = raw_report.replace(ch, "")
    report_folder = raw_report.strip()

    # ──────────────────────────────────────────────────────────────────────────
    # Build safe_subreddit (replace "/" with "_")
    # ──────────────────────────────────────────────────────────────────────────
    raw_sub = cfg.get("subreddit", "")
    safe_subreddit = raw_sub.replace("/", "_")

    # ──────────────────────────────────────────────────────────────────────────
    # Find the newest HTML report
    # ──────────────────────────────────────────────────────────────────────────
    report_path = find_latest_report(report_folder, safe_subreddit)
    if not report_path:
        print(f"No HTML report found in {report_folder}. Exiting.")
        return

    # ──────────────────────────────────────────────────────────────────────────
    # Build subject line via Jinja2
    # ──────────────────────────────────────────────────────────────────────────
    limit = cfg.get("limit", "")
    today_str = datetime.datetime.now().strftime("%Y-%m-%d")
    subj_template = cfg["email"].get("subject", "")
    subject = render_subject(subj_template, {"limit": limit, "date": today_str})

    # ──────────────────────────────────────────────────────────────────────────
    # Sender & recipients
    # ──────────────────────────────────────────────────────────────────────────
    sender = cfg["email"].get("sender")
    recipients = cfg["email"].get("recipients", [])
    if not sender or not recipients:
        print("Email sender or recipients not configured. Exiting.")
        return

    # ──────────────────────────────────────────────────────────────────────────
    # Retrieve Gmail App Password from keyring
    # ──────────────────────────────────────────────────────────────────────────
    password = keyring.get_password("reddit_report", sender)
    if not password:
        print(f"Could not find password for {sender} in keyring. Exiting.")
        return

    # ──────────────────────────────────────────────────────────────────────────
    # Initialize yagmail (Gmail)
    # ──────────────────────────────────────────────────────────────────────────
    yag = SMTP(user=sender, password=password)

    # ──────────────────────────────────────────────────────────────────────────
    # Read the latest HTML report
    # ──────────────────────────────────────────────────────────────────────────
    with open(report_path, "r", encoding="utf-8") as f:
        html_body = f.read()

    # ──────────────────────────────────────────────────────────────────────────
    # Strip out <style>…</style> so yagmail doesn’t try to interpret CSS as selectors
    # ──────────────────────────────────────────────────────────────────────────
    html_body = re.sub(r'<style.*?>.*?</style>', '', html_body, flags=re.S)

    # ──────────────────────────────────────────────────────────────────────────
    # Send email
    # ──────────────────────────────────────────────────────────────────────────
    print(f"Sending email to {recipients} with subject: {subject}")
    yag.send(
        to=recipients,
        subject=subject,
        contents=[html_body, report_path]
    )
    print("Email sent successfully!")

if __name__ == "__main__":
    main()

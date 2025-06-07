
import time

actions = ["User logged in", "Clicked settings", "Logged out"]

with open("log.txt", "a", encoding="utf-8") as log:
    for action in actions:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} — {action}\n")

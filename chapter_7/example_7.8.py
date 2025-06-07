
import logging

logging.basicConfig(level=logging.WARNING)

def login(user):
    if user != "admin":
        logging.warning("Unauthorized access attempt")
        raise PermissionError("Access Denied")

try:
    login("guest")
except PermissionError as e:
    print("Alert:", e)

# WARNING:root:Unauthorized access attempt
# Alert: Access Denied
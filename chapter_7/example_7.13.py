
import logging
import traceback

try:
    result = 10 / 0
except Exception:
    logging.error("Unexpected error:\n%s", traceback.format_exc())

# ZeroDivisionError: division by zero
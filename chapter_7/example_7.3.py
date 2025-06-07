
try:
    x = int("abc")
    y = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print("Caught an error:", type(e).__name__)

# Output: Caught an error: ValueError
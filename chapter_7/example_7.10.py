
def parse_number(user_input):
    try:
        return int(user_input)
    except ValueError as original_error:
        raise RuntimeError("Failed to parse input. Input must be a number.") from original_error

try:
    parse_number("abc")
except RuntimeError as e:
    print("Caught RuntimeError:", e)
    print("Original cause:", e.__cause__)

# Caught RuntimeError: Failed to parse input. Input must be a number.
# Original cause: invalid literal for int() with base 10: 'abc'




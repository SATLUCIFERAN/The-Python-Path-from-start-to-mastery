
try:
    value = int("abc")
    result = 10 / value
except ValueError:
    print("That's not a number.")
except ZeroDivisionError:
    print("Can't divide by zero.")

# Output: That's not a number.
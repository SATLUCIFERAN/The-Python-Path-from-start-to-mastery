
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Can't divide by zero!"
    except TypeError:
        return "Both inputs must be numbers."

print(divide(10, 2))      # 5.0
print(divide(5, 0))       # Can't divide by zero!
print(divide("a", 2))     # Both inputs must be numbers.



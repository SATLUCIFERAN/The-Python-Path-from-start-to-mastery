
def calculate_area(radius):
    assert radius >= 0, "Radius must be non-negative"
    return 3.14 * radius ** 2

print(calculate_area(5))     
print(calculate_area(-5))    

# 78.5
# AssertionError: Radius must be non-negative



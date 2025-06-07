
x = 5

def try_to_change():
    x = 10  # This is a new local variable, not the global x

try_to_change()
print(x)  # 5 (unchanged)
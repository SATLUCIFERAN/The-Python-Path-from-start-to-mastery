
y = 100

def demo():
    y = 200  # Local variable with the same name as global
    print("Inside function:", y)

demo()
print("Outside function:", y)
# Inside function: 200
# Outside function: 100

x = 5  # Global variable

def change():
    global x  # Declares we're using the global x
    x = 10

change()
print(x)  # 10

# greeting.py

def say_hello(name):
    return f"Hello, {name}!"

print("This runs no matter what.")


if __name__ == '__main__':

    print("Running test:")
    print(say_hello("Alice"))

"""
This runs no matter what.
Running test:
Hello, Alice!
"""

__name__ = 'the_module_name'
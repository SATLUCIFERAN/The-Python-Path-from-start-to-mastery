
class Dog:
    def __init__(self):
        self._energy = 100  # protected

dog = Dog()
print(dog._energy)  # ⚠️ Works, but it's discouraged
dog._energy = 50  # ⚠️ Still works - but with a warning in spirit
print(dog._energy)

# 100
# 50
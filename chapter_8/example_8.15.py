
class Dog:
    def __init__(self, name):
        self.name = name  # public

dog = Dog("Luna")
print(dog.name)  # ✅ Works: reading public attribute
dog.name = "Max"  # ✅ Works: modifying public attribute
print(dog.name)

# Luna
# Max



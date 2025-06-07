
class Dog:
    species = "Canine"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Luna")
dog2 = Dog("Max")

print(dog1.name)    # Luna
print(dog2.name)    # Max
print(dog1.species) # Canine
print(dog2.species) # Canine

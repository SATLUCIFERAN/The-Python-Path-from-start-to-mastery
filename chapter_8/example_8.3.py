
class Dog:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I'm {self.name}!")

dog1 = Dog("Luna")
dog2 = Dog("Charlie")

print(dog1.name)  # Luna
print(dog2.name)  # Charlie

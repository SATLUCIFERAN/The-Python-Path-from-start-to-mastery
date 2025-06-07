
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")


class Dog:
    def __init__(self, name="Unnamed"):
        self.name = name

    def greet(self):
        print(f"Hi, I'm {self.name}!")

nameless_dog = Dog()
nameless_dog.greet()  # Hi, I'm Unnamed!

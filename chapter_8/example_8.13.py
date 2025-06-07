
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed

    def speak(self):
        super().speak()  # Call the parent method
        print(f"{self.name} says Woof! And I'm a {self.breed}.")

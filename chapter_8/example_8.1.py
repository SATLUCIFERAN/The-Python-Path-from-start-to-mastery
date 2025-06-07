
class Dog:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I'm {self.name}!")

my_dog1 = Dog("Buddy")
my_dog1.greet()  # Hi, I'm Buddy!

my_dog2 = Dog("Lala")
my_dog2.greet()  # Hi, I'm Lala!
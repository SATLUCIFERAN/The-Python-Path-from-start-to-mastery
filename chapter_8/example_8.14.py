
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves in some way.")

class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name)  # Reuse the parent's __init__
        self.wing_span = wing_span

    def move(self):
        super().move()  # Use parent logic first
        print(f"{self.name} flies with a wingspan of {self.wing_span} meters.")

bird = Bird("Eagle", 2.3)
bird.move()

# Eagle moves in some way.
# Eagle flies with a wingspan of 2.3 meters.
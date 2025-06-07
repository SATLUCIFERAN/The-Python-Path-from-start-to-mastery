
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print(f"{self.brand} starts!")

car1 = Car("Toyota", 2020)
car1.start()  # Toyota starts!

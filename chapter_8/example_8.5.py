
class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def dog_years(age):
        return age * 7

    @property
    def info(self):
        return f"{self.name} is {self.age} years old."

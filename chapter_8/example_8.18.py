
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car drives on the road")

class Boat(Vehicle):
    def move(self):
        print("Boat sails in the water")
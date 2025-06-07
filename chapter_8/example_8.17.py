
class Dog:
    def __init__(self):
        self.__hunger = 50  # private

dog = Dog()
# print(dog.__hunger) # ❌ This will raise an AttributeError!
print(dog._Dog__hunger) # ✅ This works!

class Bird:
    def speak(self):
        print("Chirp")

class Human:
    def speak(self):
        print("Hello!")

def make_speak(entity):
    entity.speak()

make_speak(Bird()) # Chirp
make_speak(Human()) # Hello!
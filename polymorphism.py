class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

def make_sound(animal):
    return animal.sound()

# Creating objects
cat = Cat()
dog = Dog()

# Polymorphic function call
print(make_sound(cat))
print(make_sound(dog))

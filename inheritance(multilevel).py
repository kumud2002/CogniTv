class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method
dog.speak()
cat.speak()

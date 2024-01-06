class Animal:
    def speak(self):
        pass  # Base class method, to be overridden by subclasses

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Creating objects
dog = Dog()
cat = Cat()

# Polymorphic method call
print(dog.speak())  # Outputs: Woof
print(cat.speak())  # Outputs: Meow

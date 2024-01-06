class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing object attributes and calling methods
print(f"{dog1.name} is {dog1.age} years old.")
dog1.bark()
print(f"{dog2.name} is {dog2.age} years old.")
dog2.bark()

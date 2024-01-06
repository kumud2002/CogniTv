class Circle:
    def __init__(self, radius):
        self._radius = radius  # Using a single underscore to indicate it's a protected attribute

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if new_radius > 0:
            self._radius = new_radius
        else:
            print("Radius must be greater than 0.")

# Creating an object
circle = Circle(5)

# Accessing and modifying the radius using encapsulation
print("Original Radius:", circle.get_radius())
circle.set_radius(8)
print("Modified Radius:", circle.get_radius())

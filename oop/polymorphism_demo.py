import math


class Shape:
    """Base class for geometric shapes."""

    def area(self):
        """Calculate the area of the shape (to be overridden by subclasses)."""
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    """Rectangle shape that inherits from Shape."""

    def __init__(self, length, width):
        """Initialize rectangle dimensions."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape that inherits from Shape."""

    def __init__(self, radius):
        """Initialize circle radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

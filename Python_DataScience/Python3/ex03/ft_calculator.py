class calculator:
    """A calculator for vector operations with scalars."""

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, scalar):
        """Add a scalar to the vector elements."""
        result = [x + scalar for x in self.vector]
        return calculator(result)

    def __mul__(self, scalar):
        """Multiply the vector elements by a scalar."""
        result = [x * scalar for x in self.vector]
        return calculator(result)

    def __sub__(self, scalar):
        """Subtract a scalar from the vector elements."""
        result = [x - scalar for x in self.vector]
        return calculator(result)

    def __truediv__(self, scalar):
        """Divide the vector elements by a scalar."""
        result = [x / scalar for x in self.vector]
        return calculator(result)

    def __repr__(self):
        """String representation of the calculator object."""
        return str(self.vector)

    def __str__(self):
        """String representation of the calculator object for print."""
        return str(self.vector)

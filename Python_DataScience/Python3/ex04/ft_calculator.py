class calculator:
    @staticmethod
    def dotproduct(V1, V2):
        """Calculate the dot product of two vectors V1 and V2."""
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result:.1f}")

    @staticmethod
    def add_vec(V1, V2):
        """Add two vectors V1 and V2 element-wise."""
        result = [x + y for x, y in zip(V1, V2)]
        result = [f'{x:.1f}' for x in result]  # Format each element with 1 decimal place
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1, V2):
        """Subtract two vectors V1 and V2 element-wise."""
        result = [x - y for x, y in zip(V1, V2)]
        result = [f'{x:.1f}' for x in result]  # Format each element with 1 decimal place
        print(f"Sous Vector is: {result}")

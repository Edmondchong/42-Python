from S1E9 import Character

class Baratheon(Character):
    """This is a Baratheon character. They inherit from the Character class."""
    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"

    def __str__(self):
        """Return a string representation of the Baratheon character."""
        return f"Family: {self.family_name}, Eyes: {self.eyes}, Hairs: {self.hairs}"

    def __repr__(self):
        """Return a string representation of the Baratheon character for debugging."""
        return f"Baratheon: ({self.family_name}, {self.eyes}, {self.hairs})"

    def die(self):
        """Set the character's health status to not alive."""
        self.is_alive = False

class Lannister(Character):
    """This is a Lannister character. They inherit from the Character class."""
    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"

    def __str__(self):
        """Return a string representation of the Lannister character."""
        return f"Family: {self.family_name}, Eyes: {self.eyes}, Hairs: {self.hairs}"

    def die(self):
        """Set the character's health status to not alive."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create Lannister characters in a chain."""
        return cls(first_name, is_alive)

# decorator
def create_lannister(cls, first_name, is_alive=True):
    return cls.create_lannister(first_name, is_alive)

Lannister.create_lannister = classmethod(Lannister.create_lannister)
Lannister.create_lannister = staticmethod(Lannister.create_lannister)

from abc import ABC, abstractmethod

class Character(ABC):
    """This is a character class for our story."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a character with a first name and their health status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Change the character's health status to not alive."""
        self.is_alive = False

class Stark(Character):
    """This is a Stark character. They inherit from the Character class."""

    def die(self):
        """Implement the die method for Stark."""
        self.is_alive = False

from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """This is the King, a combination of Baratheon and Lannister families."""

    def __init__(self, first_name):
        super().__init__(first_name)
        
    @property
    def eyes(self):
        """Get the eye color."""
        return self._eyes

    @eyes.setter
    def eyes(self, color):
        """Set the eye color."""
        self._eyes = color

    def set_eyes(self, color):
        """Set the eye color using a method."""
        self.eyes = color

    @property
    def hairs(self):
        """Get the hair color."""
        return self._hairs

    @hairs.setter
    def hairs(self, color):
        """Set the hair color."""
        self._hairs = color

    def set_hairs(self, color):
        """Set the hair color using a method."""
        self.hairs = color

from S1E9 import Character, Stark

Ned = Stark("Ned")  # Creating a Stark character named Ned
print(Ned.__dict__)  # Printing the attributes of Ned
print(Ned.is_alive)  # Printing if Ned is alive (should be True initially)
Ned.die()  # Calling the die method to make Ned not alive (set is_alive to False)
print(Ned.is_alive)  # Printing if Ned is alive (should be False after calling die)
print(Ned.__doc__)  # Printing the docstring for the Stark class
print(Ned.__init__.__doc__)  # Printing the docstring for the constructor
print(Ned.die.__doc__)  # Printing the docstring for the die method
print("---")
Lyanna = Stark("Lyanna", False)  # Creating a Stark character named Lyanna who is initially not alive
print(Lyanna.__dict__)  # Printing the attributes of Lyanna

# Define a dictionary to store Morse code for alphanumeric characters and space
NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}

# Define a function to encode a given string into Morse code
def encode_to_morse(input_string):
    encoded_string = ""
    for char in input_string.upper():
        if char in NESTED_MORSE:
            encoded_string += NESTED_MORSE[char]
        else:
            raise AssertionError("Assertion Error:the arguments are bad")
    return encoded_string

# Check if the program is run with the correct number of arguments
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        raise AssertionError("Assertion Error:the arguments are bad")

    input_string = sys.argv[1]

    # Encode the input string to Morse code
    try:
        morse_code = encode_to_morse(input_string)
        print(morse_code)
    except AssertionError as e:
        print(e)
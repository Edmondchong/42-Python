def count_characters(argv):
    """
    Count and display the sums of uppercase, lowercase, punctuation, spaces, and digits in the input_text.

    Args:
        argv (str): The input string to analyze.

    Returns:
        None
    """
    # Initialize counts
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digit = 0

    # Iterate through each character in the input text
    for char in argv:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        elif char in ".,!?;:-":
            punctuation += 1

    # Display the results
    print(f"The text contains {len(argv)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")

def main():
    import sys

    # Check for the correct number of command-line arguments
    if len(sys.argv) == 2:
        argv = sys.argv[1]
    elif len(sys.argv) == 1:
        print("What is the text to count?")
        argv = sys.stdin.readline()
        #argv = input("What is the text to count?\n") #the input() is a prompt (wait for next input directly instead of running python filename.py "Hello" again)
    else:
        raise AssertionError("Only one argument or no argument is allowed.")

    # Call the count_characters function with the provided input
    count_characters(argv)

if __name__ == "__main__":
    main()

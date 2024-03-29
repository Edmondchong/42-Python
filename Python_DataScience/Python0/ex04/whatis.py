import sys  # Import the sys module for accessing command-line arguments

# Check if more than one argument is provided
if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
elif len(sys.argv) == 1:
    print(" ")
else:
    arg = sys.argv[1]

    try:
        arg = int(arg)

        if arg % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")

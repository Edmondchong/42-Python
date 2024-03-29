import sys
from ft_filter import ft_filter  # Import the custom ft_filter function

# Check if the correct number of arguments (2) are provided
if len(sys.argv) != 3 or not sys.argv[2].isdigit():
    print("AssertionError: the arguments are bad")
    sys.exit(1)

S = sys.argv[1]
N = int(sys.argv[2])

words = S.split()

# Use custom ft_filter and a lambda function to filter words longer than N characters
filtered_words = ft_filter(lambda word: len(word) > N, words)

print(filtered_words)
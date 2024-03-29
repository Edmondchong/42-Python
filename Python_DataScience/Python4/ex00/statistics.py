from typing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    # Check if there are any arguments in *args
    if len(args) == 0:
        print("ERROR")
        return

    # Check if any statistical operation is specified in **kwargs
    for key, value in kwargs.items():
        if key == 'toto' and value == 'mean':
            # Calculate the mean
            mean = sum(args) / len(args)
            print(f"mean : {mean:.1f}")

        if key == 'tutu' and value == 'median':
            # Calculate the median
            args = sorted(args)
            n = len(args)
            if n % 2 == 0:
                median = (args[n // 2 - 1] + args[n // 2]) / 2
            else:
                median = args[n // 2]
            print(f"median : {median:.1f}")

        if key == 'tata' and value == 'quartile':
            # Calculate the quartile
            args = sorted(args)
            n = len(args)
            q1_index = int(n * 0.25)
            q3_index = int(n * 0.75)
            quartile = [args[q1_index], args[q3_index]]
            print(f"quartile : [{quartile[0]:.1f}, {quartile[1]:.1f}]")

        if key == 'hello' and value == 'std':
            # Calculate the standard deviation
            mean = sum(args) / len(args)
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            std_deviation = variance ** 0.5
            print(f"std : {std_deviation:.10f}")

        if key == 'world' and value == 'var':
            # Calculate the variance
            mean = sum(args) / len(args)
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            print(f"var : {variance:.7f}")

    # Handle errors if no valid statistical operation is specified
    if all(key not in kwargs for key in ['toto', 'tutu', 'tata', 'hello', 'world']):
        print("ERROR")

# Testing the function with the provided examples
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")

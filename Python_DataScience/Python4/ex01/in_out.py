def square(x: int | float) -> int | float:
    return x ** 2

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function):
    count = 0
    def inner() -> float:
        nonlocal count
        count += 1
        return function(x) ** count
    return inner

def format_name(first, last):
    """
    Formats a full name from first and last name.

    Args:
        first (str): First name.
        last (str): Last name.

    Returns:
        str: Full name.
    """
    return f"{first} {last}"


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(n):
    return n % 2 == 0


def outer_function(x):
    """
    An outer function that contains a nested function.

    Args:
        x (int): Input value.

    Returns:
        int: Result.
    """
    def inner_function(y):
        return y * 2
    return inner_function(x)


class MyClass:
    def method_one(self):
        """Does something useful."""
        pass

    def method_two(self):
        pass

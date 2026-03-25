def square(x):
    """
    Returns the square of a number.

    Args:
        x (int or float): The number to square.

    Returns:
        int or float: x squared.
    """
    return x * x


def cube(x):
    """
    Returns the cube of a number.

    Args:
        x (int or float): The number to cube.

    Returns:
        int or float: x cubed.
    """
    return x * x * x


def absolute_value(x):
    if x < 0:
        return -x
    return x

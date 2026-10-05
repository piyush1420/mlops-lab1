def check_numbers(x, y):
    """Raise ValueError if x or y is not a number."""
    for value in (x, y):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Both inputs must be numbers.")


def fun1(x, y):
    """Add x and y."""
    check_numbers(x, y)
    return x + y


def fun2(x, y):
    """Subtract y from x."""
    check_numbers(x, y)
    return x - y


def fun3(x, y):
    """Multiply x and y."""
    check_numbers(x, y)
    return x * y


def fun4(x, y):
    """Return the sum of fun1, fun2 and fun3."""
    return fun1(x, y) + fun2(x, y) + fun3(x, y)


def fun5(x, y):
    """Divide x by y. Raises ValueError if y is zero."""
    check_numbers(x, y)
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

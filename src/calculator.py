"""
calculator.py - Lab 1 (modified version)
 
Changes from the original lab file:
1. Input checking is done by one helper function, _check_numbers,
   instead of repeating the same if-statement in every function.
2. True and False are now rejected. Python treats them as numbers
   (True == 1), so the original code accepted fun1(True, 2) == 3.
3. New functions:
   - fun6: raises x to the power of y
   - fun7: average of a list of numbers
   - fun9: square root of a number
"""

def check_numbers(*values):
    """
    Check that every value is an int or float (but not True/False).
    Raises:
        ValueError: If any value is not a number.
    """
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("All inputs must be numbers.")


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

def fun6(x, y):
    """Raises x to the power of y."""
    check_numbers(x, y)
    if x == 0 and y < 0:
        raise ValueError("Cannot raise 0 to a negative power.")
    return x ** y
 
 
def fun7(values):
    """
    Returns the average (mean) of a list of numbers.
    """
    if not isinstance(values, (list, tuple)) or len(values) == 0:
        raise ValueError("Input must be a non-empty list of numbers.")
    check_numbers(*values)
    return sum(values) / len(values)
 
def fun8(x):
    """
    Returns the square root of x.
    """
    check_numbers(x)
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return x ** 0.5
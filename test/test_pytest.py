import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5, 0) == 5
    assert calculator.fun1(-1, 1) == 0
    assert calculator.fun1(-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5, 0) == 5
    assert calculator.fun2(-1, 1) == -2
    assert calculator.fun2(-1, -1) == 0


def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5, 0) == 0
    assert calculator.fun3(-1, 1) == -1
    assert calculator.fun3(-1, -1) == 1


def test_fun4():
    # fun4(x, y) = fun1 + fun2 + fun3, e.g. (2+3) + (2-3) + (2*3) = 10
    assert calculator.fun4(2, 3) == 10
    assert calculator.fun4(5, 0) == 10
    assert calculator.fun4(-1, 1) == -3
    assert calculator.fun4(-1, -1) == -1


def test_fun5():
    assert calculator.fun5(10, 2) == 5
    assert calculator.fun5(7, 2) == 3.5
    assert calculator.fun5(-9, 3) == -3
    assert calculator.fun5(5.5, 2) == 2.75

    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.fun5(5, 0)

    with pytest.raises(ValueError, match="All inputs must be numbers."):
        calculator.fun5("a", 2)

    with pytest.raises(ValueError, match="All inputs must be numbers."):
        calculator.fun5(10, "b")


def test_fun6():
    assert calculator.fun6(2, 3) == 8
    assert calculator.fun6(5, 0) == 1
    assert calculator.fun6(2, -1) == 0.5
    assert calculator.fun6(9, 0.5) == 3

    with pytest.raises(ValueError, match="Cannot raise 0 to a negative power."):
        calculator.fun6(0, -1)

    with pytest.raises(ValueError, match="All inputs must be numbers."):
        calculator.fun6("a", 2)


def test_fun7():
    assert calculator.fun7([2, 4, 6]) == 4
    assert calculator.fun7([5]) == 5
    assert calculator.fun7([-1, 1]) == 0
    assert calculator.fun7([1.5, 2.5]) == 2

    with pytest.raises(ValueError, match="Input must be a non-empty list of numbers."):
        calculator.fun7([])

    with pytest.raises(ValueError, match="All inputs must be numbers."):
        calculator.fun7([1, "a", 3])


def test_fun8():
    assert calculator.fun8(16) == 4
    assert calculator.fun8(0) == 0
    assert calculator.fun8(2.25) == 1.5

    with pytest.raises(ValueError, match="Cannot take the square root of a negative number."):
        calculator.fun8(-4)

    with pytest.raises(ValueError, match="All inputs must be numbers."):
        calculator.fun8("a")


def test_rejects_true_and_false():
    with pytest.raises(ValueError, match="All inputs must be numbers."):
        calculator.fun1(True, 2)

    with pytest.raises(ValueError, match="All inputs must be numbers."):
        calculator.fun3(4, False)

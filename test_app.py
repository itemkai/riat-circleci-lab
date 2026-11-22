import pytest

from app import add, average, calculate, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


@pytest.mark.parametrize("a, b, expected", [(10, 4, 6), (0, 5, -5), (-3, -3, 0)])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


def test_multiply():
    assert multiply(4, 2.5) == 10
    assert multiply(7, 0) == 0


def test_divide():
    assert divide(9, 3) == 3
    assert divide(1, 4) == 0.25


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_average():
    assert average([2, 4, 6]) == 4
    with pytest.raises(ValueError):
        average([])


@pytest.mark.parametrize("expr, expected", [("2 + 3", 5), ("10 / 4", 2.5), ("3 * 3", 9), ("8 - 10", -2)])
def test_calculate(expr, expected):
    assert calculate(expr) == expected


def test_calculate_unknown_operation():
    with pytest.raises(ValueError):
        calculate("2 ^ 3")

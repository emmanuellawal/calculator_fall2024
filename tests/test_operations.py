# tests/test_operations.py

import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    """Test the addition function with positive numbers."""
    assert addition(1, 2) == 3

def test_addition_negative():
    """Test the addition function with negative numbers."""
    assert addition(-1, -2) == -3

def test_addition_zero():
    """Test the addition function with zero."""
    assert addition(0, 5) == 5

def test_subtraction():
    """Test the subtraction function with positive numbers."""
    assert subtraction(5, 3) == 2

def test_subtraction_negative():
    """Test the subtraction function with negative numbers."""
    assert subtraction(-5, -3) == -2

def test_subtraction_result_negative():
    """Test the subtraction function resulting in a negative number."""
    assert subtraction(3, 5) == -2

def test_multiplication():
    """Test the multiplication function with positive numbers."""
    assert multiplication(3, 4) == 12

def test_multiplication_negative():
    """Test the multiplication function with a negative number."""
    assert multiplication(-3, 4) == -12

def test_multiplication_zero():
    """Test the multiplication function with zero."""
    assert multiplication(0, 100) == 0

def test_division():
    """Test the division function with positive numbers."""
    assert division(10, 2) == 5

def test_division_negative():
    """Test the division function with a negative numerator."""
    assert division(-10, 2) == -5

def test_division_result_fraction():
    """Test the division function resulting in a fraction."""
    assert division(7, 2) == 3.5

def test_division_by_zero_exception():
    """Test that division by zero raises a ValueError."""
    with pytest.raises(ValueError) as exc_info:
        division(10, 0)
    assert str(exc_info.value) == "Division by zero is not allowed."

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (-1, -1, -2),
        (0, 0, 0),
        (123456, 654321, 777777),
    ],
)
def test_addition_parametrized(a, b, expected):
    """Parametrized test for the addition function."""
    assert addition(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (-5, -3, -2),
        (3, 5, -2),
        (0, 0, 0),
    ],
)
def test_subtraction_parametrized(a, b, expected):
    """Parametrized test for the subtraction function."""
    assert subtraction(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 12),
        (-3, 4, -12),
        (0, 100, 0),
        (123, 456, 56088),
    ],
)
def test_multiplication_parametrized(a, b, expected):
    """Parametrized test for the multiplication function."""
    assert multiplication(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (-10, 2, -5),
        (7, 2, 3.5),
        (0, 1, 0),
    ],
)
def test_division_parametrized(a, b, expected):
    """Parametrized test for the division function."""
    assert division(a, b) == expected

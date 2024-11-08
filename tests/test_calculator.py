# tests/test_calculator.py

import sys
import os
import pytest

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(1, 1) == 2

def test_subtraction():
    assert subtraction(1, 1) == 0

def test_multiplication():
    assert multiplication(1, 2) == 2

def test_division():
    assert division(1, 1) == 1

def test_division_by_zero_exception():
    with pytest.raises(ValueError):
        division(10, 0)
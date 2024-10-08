''' My Calculator Test'''
import pytest
from app.main import addition, division, multiplication, subtraction

def test_addition():
    '''Addition function'''
    assert addition(1,1) == 2

def test_subtraction():
    '''Subtraction function'''
    assert subtraction(1,1) == 0

def test_multiplication():
    '''Multiplication function'''
    assert multiplication(1,2) == 2

def test_division():
    '''Division function'''
    assert division(1,1) == 1

def test_division_by_zero_exception():
    '''Division function testing that I get the exception divide by zero'''
    with pytest.raises(ZeroDivisionError):
        division(10,0)

""" Module for testing functionality """

import pytest
from src.main import is_odd, bubble_sort, has_duplicates, insertion_sort, double_array, factorial, sum_of_chars, max_number, fibonacci, fibonacci_v2, array_sum

@pytest.mark.parametrize(
    "number, result",
    [(3, True), (8, False)]
)
def test_is_odd_number(number, result):
    """ Check for odd numbers """
    assert is_odd(number) is result

@pytest.mark.parametrize(
    "original_array, asc, sorted_array",
    [
        ([4, 2, 7, 1, 3], False, [7, 4, 3, 2, 1]), 
        ([65, 55, 45, 35, 25, 15, 10], True, [10, 15, 25, 35, 45, 55, 65])
    ]
)
def test_bubble_sort(original_array, asc, sorted_array):
    """ Test sorting with bubble sort """
    assert bubble_sort(original_array, asc) == sorted_array

@pytest.mark.parametrize(
    "original_array, result",
    [
        ([4, 2, 7, 1, 3], False),
        ([65, 55, 45, 35, 25, 15, 10, 55], True)
    ]
)
def test_has_duplicates(original_array, result):
    """ Check for duplicates """
    assert has_duplicates(original_array) == result

@pytest.mark.parametrize(
    "original_array, asc, sorted_array",
    [
        # ([4, 2, 7, 1, 3], False, [7, 4, 3, 2, 1]),
        ([65, 55, 45, 35, 25, 15, 10], True, [10, 15, 25, 35, 45, 55, 65])
    ]
)
def test_insertion_sort(original_array, asc, sorted_array):
    """ Test sorting with insertion sort """
    assert insertion_sort(original_array, asc) == sorted_array

def test_double_array():
    """ Test doubling array in memory """
    test_array = [1, 2, 3, 4, 5]

    double_array(test_array)

    assert test_array == [2, 4, 6, 8, 10]

def test_sum_of_chars():
    """ Test sum of all characters in array """
    result = sum_of_chars(['ab', 'c', 'def', 'ghij'])
    assert result == 10

def test_max_number():
    """ Test maximum number in array """
    result = max_number([1, 2, 3, 4, 5])
    assert result == 5

def test_factorial():
    """ Test factorial of a given number """
    result = factorial(4)
    assert result == 24

def test_fibonacci():
    """ Test the fibonacci sequence """
    result_1 = fibonacci(5)
    assert result_1 == 5

    result_2 = fibonacci_v2(6)
    assert result_2 == 8

def test_array_sum():
    """ Test sum of all integers """
    result = array_sum([1, 2, 3])
    assert result == 6

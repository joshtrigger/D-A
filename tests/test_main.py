""" Module for testing functionality """

import pytest
from src.main import is_odd, bubble_sort, has_duplicates

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

""" Practice examples on Data Structures & Algorithms """

def is_odd(num):
    """ Checks for odd numbers using binary search """
    for i in range(2, num):
        if num % i == 0:
            return False
        return True


def bubble_sort(array, asc=True):
    """
    Sorts arrays of numbers in ascending order using bubble sort 

    Args:
        array (list): arrray to be sorted

    Returns:
        list: sorted array
    """
    last_index = len(array) - 1
    is_sorted = False

    while not is_sorted:
    # for each pass though, assume the array is is_sorted until swap is performed
        is_sorted = True
        for i in range(last_index):
            condition = array[i] > array[i + 1] if asc else array[i] < array[i + 1]
            # check if value on left is greater than value on right
            if condition:
                array[i], array[i + 1] = array[i + 1], array[i] # perform the swap
                is_sorted = False
        last_index -= 1 # move right most index to the left after pass through
    return array

def has_duplicates(array):
    """ Checks for duplicates in an array """
    for i, num_i in enumerate(array):
        for j, num_j in enumerate(array):
            if i != j and num_i == num_j:
                return True
    return False

def insertion_sort(array, asc = True):
    """ Sorting an array with insertion sort """
    count = 0
    for index in range(1 if asc else len(array) - 2, len(array) if asc else 1, 1 if asc else -1):
        temp_value = array[index]
        position = index - 1 if asc else index + 1

        while position >= 0 if asc else position < len(array):
            count+=1
            if array[position] > temp_value:
                array[position + 1 if asc else position - 1] = array[position]
                position = position - 1 if asc else position + 1
            else :
                break

        array[position + 1 if asc else position - 1] = temp_value
    return array

def double_array(array: list[int], index = 0) -> list[int]:
    """ Doubling array in memory """
    # Base case is when index is past end of array
    if index >= len(array):
        return
    array[index] *= 2
    double_array(array, index + 1)

def factorial(number: int) -> int:
    """ Calculating factorial of number using recursion """
    if number == 1:
        return 1
    return number * factorial(number - 1)

def array_sum(array: list[int]) -> int:
    """ Calculate sum of all integers in array """
    if len(array) == 0:
        return 0
    return array[0] + array_sum(array[1: len(array)])

def sum_of_chars(array_of_strings:list[str]) -> int:
    """ Function that calculates the sum of all characters in an array """
    if len(array_of_strings) == 0:
        return 0

    return len(array_of_strings[0]) + sum_of_chars(array_of_strings[1 : len(array_of_strings)])

def max_number(array_of_numbers: list[int]) -> int:
    """ Returns maximum number in an array """
    if len(array_of_numbers) == 1:
        return array_of_numbers[0]

    calculated_max = max_number(array_of_numbers[1: len(array_of_numbers)])

    if array_of_numbers[0] > calculated_max:
        return array_of_numbers[0]
    return calculated_max

def fibonacci(number: int) -> int:
    """ Calculate fibonacci sequence, without memoization """
    if number in (0 ,1):
        return number

    return fibonacci(number - 2) + fibonacci(number - 1)

def fibonacci_v2(number: int, memo: dict = {}) -> int:
    """ Calculate fibonacci sequence, with memoization """
    if number in (0 ,1):
        return number

    if number not in memo:
        memo[number] = fibonacci_v2(number - 2) + fibonacci_v2(number - 1)

    return memo[number]

class SortArray():
    """ Used for quick sort """

    def __init__(self, array) -> None:
        self.array = array

    def partition(self, left_pointer, right_pointer):
        """ used to partition an array """

        pivot_index = right_pointer
        pivot = self.array[right_pointer]

        right_pointer -= 1

        while True:

            while self.array[left_pointer] < pivot:
                left_pointer += 1

            while self.array[right_pointer] > pivot:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]

            left_pointer += 1

        self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]

        return left_pointer

    def quick_sort(self, left_index, right_index):
        """ Performs quick sort """

        if right_index - left_index <= 0:
            return

        pivot_index = self.partition(left_index, right_index)

        self.quick_sort(left_index, pivot_index - 1)

        self.quick_sort(pivot_index + 1, right_index)

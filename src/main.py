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

def double_array(array, index = 0):
    # Base case is when index is past end of array
    if index >= len(array):
        return
    array[index] *= 2
    double_array(array, index + 1)

def factorial(number):
    """"""
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

def array_sum(array):
    return array[0] + array_sum(array[1:len(array)-1])

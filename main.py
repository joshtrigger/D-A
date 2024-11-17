""" Practice examples on Data Structures & Algorithms """

def is_odd(num):
    """ Checks for odd numbers using binary search aka O(logN) """

    for i in range(2, num):
        if num % i == 0:
            return False
        return True

print('Check for odd number with simple binary search example \n')
print(4, '==>' ,  is_odd(4))
print(9, '==>' ,  is_odd(9))
print()

def bubble_sort(array, asc=True):
    """
    Sorts arrays of numbers in ascending order using bubble sort aka O(N^2)

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

print('Sort arrays using bubble sort \n')
print([4, 2, 7, 1, 3], '==>' , bubble_sort([4, 2, 7, 1, 3], False))
print([65, 55, 45, 35, 25, 15, 10], '==>' ,  bubble_sort([65, 55, 45, 35, 25, 15, 10]))
print()

def has_duplicates(array):
    """ Checks for duplicates in an array using O(N^2) """
    for i, num_i in enumerate(array):
        for j, num_j in enumerate(array):
            if i != j and num_i == num_j:
                return True
    return False

print('Check if array has duplicates using O(N^2)')
print([1, 2, 4, 5, 6], '==>' , has_duplicates([1, 2, 4, 5, 6]))
print([1, 2, 4, 5, 2], '==>' , has_duplicates([1, 2, 4, 5, 2]))
print()

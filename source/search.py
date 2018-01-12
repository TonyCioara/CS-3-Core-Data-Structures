import random


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if array[index] == item:
        return index
    if index < len(array) - 1:
        return linear_search_recursive(array, item, index + 1)
    return None
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    first_index = 0
    last_index = len(array) - 1
    to_return_none = False

    while last_index - first_index >= 1:
        if last_index - first_index == 1:
            to_return_none = True
        new_index = (last_index + first_index) / 2
        check_for_2_numbers = False
        if new_index % 1 != 0:
            check_for_2_numbers = True

        new_index = int(new_index)
        print(first_index, " ", last_index)
        if array[new_index] == item:
            return new_index
        elif array[new_index] > item:
            last_index = new_index
        elif array[new_index] < item:
            if check_for_2_numbers is True:
                if array[new_index + 1] == item:
                    return new_index + 1
                first_index = new_index + 1
            first_index = new_index
        if to_return_none is True:
            return None
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None, to_return_none=False):
    # TODO: implement binary search recursively here
    if left is None:
        left = 0
        right = len(array) - 1
    if to_return_none is True:
        return None
    if right - left == 1:
        to_return_none = True
    new_index = (right + left) / 2
    check_for_2_numbers = False
    if new_index % 1 != 0:
        check_for_2_numbers = True
    new_index = int(new_index)
    if array[new_index] == item:
        return new_index
    elif array[new_index] > item:
        return binary_search_recursive(array, item, left, new_index, to_return_none)
    elif array[new_index] < item:
        if check_for_2_numbers is True:
            if array[new_index + 1] == item:
                return new_index + 1
            return binary_search_recursive(array, item, new_index + 1, right, to_return_none)
        return binary_search_recursive(array, item, new_index, right, to_return_none)
    return None

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


if __name__ == '__main__':
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    print(binary_search_recursive(names, "Nicke"))

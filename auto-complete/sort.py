"""
file:        sort.py
description: Uses merge sort to sort the list of 
             words in O(nlogn) time.
author:      Abhijay Nair, an1147@rit.edu
author:      Sushruth Beeti, sb3112@rit.edu
"""


def merge_sort(data):
    """
    Recursively calls merge_sort until a single element is
    present in the list and once both halves are of length 1
    the merge process begins
    :param: data, the data to be sorted
    :return: returns the sorted list
    """
    # End recursion if only a single element is present
    if len(data) < 2:
        return data
    else:
        # Split the list into two halves
        left, right = split(data)
        # Split until a single element is present
        # Build up the sorted list from there
        return merge(merge_sort(left), merge_sort(right))


def split(data):
    """
    Splits the list into two halves
    :param: data, the list of words to be split
    :return: tuple of left half of the list and right half of the list
    """
    return data[:len(data) // 2], data[len(data) // 2:]


def merge(left, right):
    """
    Merges the two halves of the list while sorting them.
    :param: left sublist
    :param: right sublist
    :return: sorted list from sub lists
    """
    left_index = 0
    right_index = 0
    result = []
    # Copy the smaller element amongst the left and the right half
    # and add to the list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    # Copy any elements remaining in the left half
    if left_index < len(left):
        result.extend(left[left_index:])
    # Copy any elements remaining in the right half
    if right_index < len(right):
        result.extend(right[right_index:])
    return result


def get_sorted_list(words_list):
    """
    The main function calls the merge_sort method to sort the
    list of words
    :param: words_list, the list of words to be sorted
    :return: an lexicographically sorted list of words
    """
    # Convert the words to lower case
    words = [word.strip().lower() for word in words_list]
    # Sort the list and return the sorted list
    return merge_sort(words)

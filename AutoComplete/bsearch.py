"""
file:        bsearch.py
description: Searches for a word with a matching prefix
             in the given list of sorted words
language:    python3
author:      Abhijay Nair, an1147@rit.edu
author:      Sushrut Beeti, sb3112@rit.edu
"""


def prefix_matches(word, prefix):
    """
    Checks whether the prefix given is a prefix of the
    currently passed word
    :param: word (string), the word in the list
    :param: prefix (string), the prefix being checked
    :return: boolean, True if is a prefix, else return False
    """
    if len(word) < len(prefix):
        return False
    for index, char in enumerate(prefix):
        if word[index] != prefix[index]:
            return False
    return True


def binary_search(words, prefix, left, right):
    """
    The recursive binary search function which tries to
    find a word with a prefix which matches the prefix
    provided by the user.
    :param: words (list), list of sorted words
    :param: prefix (string), prefix to be matched with
    :param: left (int), start index
    :param: right (int), ending index
    :return: index of the first word with a matching prefix,
             -1 if not found
    """
    if left > right:
        return -1
    mid = (left + right) // 2

    # The prefix is matched with the previous word to ensure the first word with
    # the given prefix is considered
    if prefix_matches(words[mid], prefix) and not prefix_matches(words[mid - 1], prefix):
        return mid

    # Explore the first half of the list if data in the middle is greater
    # than the prefix
    elif words[mid] > prefix:
        return binary_search(words, prefix, left, mid - 1)

    # Explore the right half of the words
    else:
        return binary_search(words, prefix, mid + 1, right)


def main(words, prefix):
    """
    Calls the binary_search() method to find the index of the element
    :param: words (list), a list of sorted words
    :param: prefix (string), prefix to be matched with
    :return: index of the first word with a matching prefix,
             -1 if not found
    """
    return binary_search(words, prefix, 0, len(words) - 1)

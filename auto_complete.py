"""
file:        auto_complete.py
description: Implements the auto-complete featue
             to return words that match user given
             prefixes
language:    python3
author:      Abhijay Nair, an1147@rit.edu
author:      Sushruth Beeti, sb3112@rit.edu
"""

import sys
import sort
import bsearch


def find_words_with_a_prefix(current_prefix, previous_prefix, start_match_index,
                             current_match_index, words):
    """
    This method takes in the input string and prints the corresponding
    word according to the prefix. Two other indices are used to perform
    the linear search for the next word in the list of words if no
    prefix is provided
    :param: current_prefix (string), user-given prefix
    :param: previous_prefix (string), previously given prefix
    :param: start_match_index, the index of the first matched word
    :param: current_match_index, current index match of word
    :param: words (list), list of available words
    :return: tuple of word in the list of given prefix,
             current prefix,
             index of the first match with a prefix,
             current match index
    """
    current_prefix = current_prefix.lower()
    if current_prefix == '':
        if not bsearch.prefix_matches(words[current_match_index], previous_prefix):
            current_match_index = start_match_index
        return words[current_match_index], previous_prefix, start_match_index, current_match_index + 1
    else:
        # Find the word in the list with the given prefix
        match_start_index = bsearch.main(words, current_prefix)
        # If no valid word is found, from next time if empty string is hit
        # every word in list is returned one by one for every empty string inputted
        if match_start_index == -1:
            return 'No match', '', 0, 0
        return words[match_start_index], current_prefix, match_start_index, match_start_index + 1


def auto_complete(words):
    """
    This method sorts and displays the available words using the sort class
    Then, the user is prompted for an input trying to elicit a prefix
    and then the the prefix is processed to find a word starting with that
    prefix.
    :param: words, the list of available words
    """
    sorted_words_list = sort.get_sorted_list(words)
    print('The sorted list :\n')
    print('----------------------------------------------------------------')
    print(sorted_words_list)
    print('----------------------------------------------------------------')
    print('Welcome to Autocomplete!')
    print('usage: Enter a prefix to autocomplete')
    print('Entering empty string will print all valid words for previous match one by one')
    print('Enter <QUIT> to exit')
    user_prompt_string = 'Enter a prefix to search for: '
    previous_prefix = ""
    current_prefix = input(user_prompt_string)
    current_match_index = 0
    start_match_index = 0
    while current_prefix != '<QUIT>':
        # Get the index of the target word
        word, previous_prefix, start_match_index, current_match_index = \
            find_words_with_a_prefix(current_prefix,
                                     previous_prefix,
                                     start_match_index,
                                     current_match_index,
                                     sorted_words_list)
        print(word.capitalize())
        current_prefix = input(user_prompt_string)
    print('Exiting Auto-complete! Good bye.')


def main():
    """
    The main method reads the command line arguments and tries to
    read the words from the file given as a parameter. Then,
    the autocomplete feature is started. The program exits if
    incorrect arguments are provided.
    """

    # Check if correct number of arguments are present
    if len(sys.argv) != 2:
        print('usage: auto_complete.py filename.txt')
        sys.exit()

    # Get the filename from the command line
    filename = sys.argv[1]

    # Remove duplicates from the list
    words_list = set()

    try:
        # Open the file and save the words in a list
        with open(filename) as f:
            for word in f:
                words_list.add(word[:-1])
    except FileNotFoundError:
        print("Failed to open the file provided.")
        sys.exit()

    # Start the autocomplete feature
    auto_complete(list(words_list))


if __name__ == '__main__':
    main()

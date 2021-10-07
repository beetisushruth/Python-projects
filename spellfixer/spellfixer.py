"""
file: spellfixer.py
language: python3
description: Corrects the spelling mistake for three cases:
1) Neighbor key hit by mistake
2) Multiple key hit of the same character by mistake
3) Replace one letter for other non-neighbor character

Test Cases:
1) The qu9ck brrown foxx jumped ovver ths lazzzy sog!!!
  The quick brown fix, jumped over the lazy dog
2) H9w a4e youuu???. -> How are you???
3) Healo Wxrld!!-> Hello World!!
author: Sushruth Beeti (sb3112@rit.edu)
author: Abhijay Nair (an1147@rit.edu)
"""

import sys
import re


def read_files(english_word_file, keyboard_distribution_file):
    """
    Reads the files english word file and keyboard distribution file
    :param english_word_file:   english word file
    :param keyboard_distribution_file:  keyboard distribution file
    :return: english word set and adjacent character dictionary
    """
    english_words_set = set()
    adjacent_character_dict = dict()
    try:
        with open(english_word_file) as f:
            for line in f:
                line = line.strip()
                words = line.split(" ")
                for word in words:
                    english_words_set.add(word.lower())
        with open(keyboard_distribution_file) as f:
            for line in f:
                line = line.strip()
                characters = line.split(" ")
                adjacent_character_dict[characters[0].lower()] = \
                    [character.lower() for character in characters[1:]]
    except Exception as e:
        print("Reading file failed!")
    return english_words_set, adjacent_character_dict


def isWordAPunctuation(word):
    """
    Checks if the word is not alphabet but a punctuation
    :param word: word
    :return: boolean
    """
    return re.match("([.,!?;'\" ])+", word) is not None


def get_alternative_correct_word(word, english_words_set,
                                 adjacent_character_dict):
    """
    Get alternative corrected word for neighbor key hit case
    :param word:    word to be corrected
    :param english_words_set:   set of english words
    :param adjacent_character_dict: adjacent character dictionary
    :return: modified word
    """
    # iterate over the characters
    for index, character in enumerate(word):
        # get adjacent character for the character
        adjacent_characters = adjacent_character_dict[character.lower()]
        # make different word combinations
        for adjacent_character in adjacent_characters:
            cased_adjacent_character = adjacent_character \
                if character.islower() or character.isnumeric() \
                else adjacent_character.upper()
            new_word = word[:index] + cased_adjacent_character + \
                       word[index + 1:]
            if new_word.lower() in english_words_set:
                return new_word
    return word


def fix_neighbor_key_hit(word_array, english_words_set, adjacent_character_dict):
    """
    Fix neighbor key hit case
    :param word_array:  word array
    :param english_words_set:   set of english words
    :param adjacent_character_dict: adjacent characters dictionary
    :return:    modified word array
    """
    for index, word in enumerate(word_array):
        if word.lower() not in english_words_set and not isWordAPunctuation(word):
            word_array[index] = get_alternative_correct_word(
                word, english_words_set,
                adjacent_character_dict)
    return word_array


def remove_duplicates(word, english_words_set):
    """
    Remove duplicate characters from a word
    :param word:    word string
    :param english_words_set:   set with english words
    :return:    modified word
    """
    index = 0
    while index < len(word):
        character_count = 1
        while index + 1 < len(word) and \
                word[index + 1].lower() == word[index].lower():
            character_count += 1
            index += 1
        if character_count > 1:
            for i in range(1, character_count):
                new_word = word[:index + i - character_count] + word[index:]
                if new_word.lower() in english_words_set:
                    return new_word \
                        if word[0].islower() else new_word.capitalize()
        index += 1
    return word


def fix_duplicate_key_hit(word_array, english_words_set):
    """
    Fix duplicate key hit method
    :param word_array:  word array
    :param english_words_set:   set with english words
    :return:    modified word array
    """
    for index, word in enumerate(word_array):
        if word.lower() not in english_words_set and not isWordAPunctuation(word):
            word_array[index] = remove_duplicates(word, english_words_set)
    return word_array


def check_alt_char(word, english_words_set):
    """
    Fix the error caused by replacing any character with another
    :param word:  word string
    :param english_words_set:   set with english words
    :return:    modified word
    """

    # convert into into lower case
    edited_word = list(word)
    alphabets = [chr(x) for x in range(97, 123)]
    # go through every alphabet for each character
    # and check if it's a valid word
    for index, char in enumerate(edited_word):
        for alphabet in alphabets:
            edited_word[index] = alphabet \
                if word[index].islower() or \
                   word[index].isnumeric() else alphabet.upper()
            if ''.join(edited_word).lower() in english_words_set:
                return ''.join(edited_word)
            else:
                edited_word[index] = word[index]
    return word


def replace_letter(word_array, english_words_set):
    """
    Replace a character of the word with any other character to check
    a possible correct word. Characters are not necessarily keyboard
    neighbors
    :param word_array:  word array
    :param english_words_set:   set with english words
    :return:    modified word array
    """

    for index, word in enumerate(word_array):
        if word.lower() not in english_words_set and not isWordAPunctuation(word):
            word_array[index] = check_alt_char(word, english_words_set)
    return word_array


def split_with_punctuations(input_sentence):
    """
    Splits a sentence with punctuations and spaces
    (also has punctuations in the array)
    :param input_sentence:  input sentence string
    :return:    string array
    """
    return re.findall(r"[\w']+|[.,!?;' ]", input_sentence)


def run_spellfixer(english_words_set, adjacent_character_dict):
    """
    Runs the spell fixer method and corrects three unique spelling mistakes
    :param english_words_set:   set containing english words
    :param adjacent_character_dict: Dictionary with adjacent keyboard keys
    :return: None
    """
    print("Welcome to spell fixer...")
    input_sentence = input()
    while input_sentence != "!*!":
        # get words split in a sentence (also has punctuations in the array)
        word_array = split_with_punctuations(input_sentence)
        # fix words for when a neighbor key was hit
        # Replace character of a word with another
        word_array = fix_neighbor_key_hit(word_array,
                                          english_words_set,
                                          adjacent_character_dict)
        # fix words that has duplicate keys
        word_array = fix_duplicate_key_hit(word_array, english_words_set)
        word_array = replace_letter(word_array, english_words_set)
        print(''.join(word_array))
        input_sentence = input()
    print("Exiting spell fixer")


def main():
    """
    Main method to run spell fixer
    :return:    None
    """
    arguments = sys.argv
    try:
        # english word file source
        english_word_file = arguments[1]
        # keyboard distribution file source
        keyboard_distribution_file = arguments[2]
    except Exception as e:
        print("Invalid arguments provided!", e)
    # read both files
    english_words_set, adjacent_character_dict = \
        read_files(english_word_file, keyboard_distribution_file)
    # run spell fixer
    run_spellfixer(english_words_set, adjacent_character_dict)


if __name__ == "__main__":
    main()

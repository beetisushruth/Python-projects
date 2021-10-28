"""
file: tests.py
description: Verify the chained hash map class implementation
"""

__author__ = ["Sushruth Beeti", "Abhijay Nair"]

from hashmap import HashMap


def print_map(a_map):
    for word, counter in a_map:  # uses the iter method
        print(word, counter, end=" ")
    print()


def test0():
    """
    Provided by the instructor
    :return: None
    """
    table = HashMap(initial_num_buckets=10)
    table.add("to", 1)
    table.add("do", 1)
    table.add("is", 1)
    table.add("to", 2)
    table.add("be", 1)

    print_map(table)

    print("'to' in table?", table.contains("to"))
    print("'to' appears", table.get("to"), "times")
    table.remove("to")
    print("'to' in table?", table.contains("to"))

    print_map(table)


def test1():
    """
    Test case where initial number of buckets are not provided
    And it would default to 100. And testing corner cases of removing
    an element when the set is empty
    :return: None
    """
    print(
        """\nTest#1: Test case where initial number of buckets are not provided. 
        And it would default to 100. And testing corner cases of removing an element when the hash map is empty """)
    table = HashMap()
    print(table.table_size)
    table.add("a", 1)
    table.add("a", 100)
    table.add("a", 1)
    table.add("a", 4)
    print_map(table)
    table.remove("a")
    print("'a' in table?", table.contains("a"))
    # should work as normal without raising error, should just return without
    # doing anything to the hashmap
    table.remove("a")
    print("'a' in table?", table.contains("a"))
    print('size', table.size)


def test2():
    """
    Test case would check the correctness of hash function,
    if it is filling up all the cells if provided spread out keys
    :return: None
    """
    print(
        """\nTest#2: HashMap of size 26 is created, and keys of 'a-z' are inserted to check the spread of the keys in 
        hashmap. Ideally for our hash function it should be 0 imbalance""")
    table = HashMap()
    for i in range(0, 26):
        table.add(str(chr(ord('a') + i)), 1)
    print_map(table)
    print("'a' in table?", table.contains("a"))
    print("'z' in table?", table.contains("z"))
    print("Imbalance in hashmap: ", table.imbalance())


def test3():
    """
    Test case to check the repr method and iterator functionality for the
    hash map
    :return: None
    """
    print(
        """\nTest#3: Testcase will check the iterator function implementation and repr method""")
    table = HashMap()
    for i in range(0, 26):
        table.add(str(chr(ord('a') + i)), 1)
    print(table)
    for key, value in table:
        print(key, value)


def test4():
    """
    Test case to test rehashing/resizing functionality
    :return:
    """
    print(
        """\nTest#4: Testcase 4 will check the resizing by printing the table mid way, and printing table once after 
        it is finished""")
    table = HashMap(initial_num_buckets=13)
    for i in range(0, 13):
        table.add(str(chr(ord('a') + i)), 1)
    print(table)
    print("Imbalance:", table.imbalance())
    for i in range(12, 26):
        table.add(str(chr(ord('a') + i)), 1)
    print(table)
    print("Imbalance:", table.imbalance())


def test5():
    """
    Test case to test if the size decreases less than MIN_BUCKETS length
    :return:
    """
    print(
        """\nTest#5: Testcase 5 will check if the size decreases less than MIN_BUCKETS length
        which it should not""")
    table = HashMap(initial_num_buckets=5)
    print("Size: ", table.table_size, "(doesn't go below 10)")
    table.add("a", 1)
    table.remove("a")
    print("Size: ", table.table_size, "(doesn't go below 10)\n")
    print(table)


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()

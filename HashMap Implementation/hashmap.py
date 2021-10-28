"""
file: hashmap.py
language: python3
description: A homemade hash map that uses chaining for handling collisions
author: Sushruth Beeti (sb3112@rit.edu)
author: Abhijay Nair (an1147@rit.edu)
"""
from collections.abc import Iterable
from typing import Callable, Hashable, Iterator, Tuple, Any


class ChainNode:
    __slots__ = "key", "value", "link"  # explicitly mentioning the class variable

    def __init__(self, key: str, value: any, link=None):
        """
        Constructor for ChainNode
        :param value: value
        :param link: link
        """
        self.key = key
        self.value = value
        self.link = link

    def __repr__(self):
        """
        Linked Node representation method
        :return: representation of ChainNode
        """
        return "ChainNode(" + "key: " + self.key + ", value: " + str(self.value) + ")"


# This chain list implementation only contains functionality that are required for HashMap implementation

class ChainList:
    __slots__ = "front"

    def __init__(self):
        """
        Constructor for ChainList
        """
        self.front = None

    def __repr__(self):
        """
        Implementation of repr of the list
        :return: str
        """
        nodes = "ChainList["
        node = self.front
        while node is not None:
            nodes += (str(node) + " -> ")
            node = node.link
        nodes += "None]"
        return nodes

    def __len__(self):
        """
        Implementation to get the length of the chain list
        :return: length
        """
        current_node = self.front
        count = 0
        # get the length of the linked list
        while current_node is not None:
            current_node = current_node.link
            count += 1
        return count

    def __iter__(self):
        """
        Iteration implementation for ChainList
        :return: iterable of nodes
        """
        node = self.front
        # iterate over the list and yield
        # key and value
        while node is not None:
            yield node.key, node.value
            node = node.link

    def prepend(self, key, value) -> None:
        """
        Prepend the key, value to the list
        :param key: key
        :param value: value
        :return: None
        """
        self.front = ChainNode(key, value, self.front)

    def get(self, key: Hashable) -> Any:
        """
        Get the value of the key else return none
        :param key: key
        :return: value
        """
        current_node = self.front
        # iterate and get the node value
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.link
        return None

    def update_if_key_exists(self, key: str, value: int):
        """
        Update if key exists in the list
        :param key: key
        :param value: value
        :return: bool
        """
        current_node = self.front
        # check for a key, and update it's node value to the new value
        while current_node is not None:
            if current_node.key == key:
                current_node.value = value
                return True
            current_node = current_node.link
        return False

    def remove(self, key):
        """
        Remove the node from the chain list
        :param key: remove this value
        :return: None
        """
        current_node = self.front
        previous_node = None
        # remove the current node while it is not None
        while current_node is not None:
            if current_node.key == key:
                # if previous node is none, that means it is the first node
                if previous_node is None:
                    self.front = current_node.link
                else:
                    previous_node.link = current_node.link
            # incrementing previous node and current node
            previous_node = current_node
            current_node = current_node.link

    def contains(self, key):
        """
        Check if key is contained in this chain list
        :param key: key
        :return: bool
        """
        current_node = self.front
        # iterate the list and check if the element is present
        while current_node is not None:
            if current_node.key == key:
                return True
            current_node = current_node.link
        return False


def hash_A(key):
    """
    Hash function during the problem solving session
    :param key: key
    :return: hash value
    """
    hash_sum = 0
    for index, character in enumerate(key):
        hash_sum += ord(character)
    return hash_sum


def hash_B(key):
    """
    Hash function during the problem solving session
    :param key: key
    :return: hash value
    """
    hash_sum = 0
    for index, character in enumerate(key):
        hash_sum += ord(character) * (31 ** index)
    return hash_sum


class HashMap(Iterable):
    __slots__ = "hash_func", "table_size", "hash_table", "size", "load_limit", "MIN_BUCKETS"

    def __init__(self, hash_func: Callable[[str], int] = hash_B,
                 initial_num_buckets: int = 100, load_limit: float = 0.75) -> None:
        """
        Constructor for HashMap implementation
        :param hash_func:  hash function to be used,
        has a dummy default hash function just in case
        :param initial_num_buckets: size of hash table to be used
        """
        self.MIN_BUCKETS = 10
        self.hash_table = [None] * max(initial_num_buckets, self.MIN_BUCKETS)
        self.table_size = max(initial_num_buckets, self.MIN_BUCKETS)
        self.hash_func = hash_func
        self.load_limit = load_limit
        self.size = 0

    def __repr__(self) -> str:
        """
        Repr of the hash map
        :return: str
        """
        hash_map = ""
        for index, cell in enumerate(self.hash_table):
            hash_map += ("index: " + str(index) + " => " + str(cell) + "\n")
        return hash_map

    def __iter__(self) -> Iterator[Tuple[Hashable, Any]]:
        """
        Build an iterator
        :return: an iterator for the current entries in the map
        """
        for cell in self.hash_table:
            if cell is not None:
                # using the linkedlist iter method
                for key, value in cell:
                    yield key, value

    def add(self, key: Hashable, value: Any) -> None:
        """
        Insert a new entry into the hash table. However, if the key
        already exists, the value associated to that key is updated with the given value.
        :param key: key to add
        :param value: value to add
        :return: None
        """
        # get hash key
        hash_key = self.hash_func(key) % self.table_size
        # invoke the add utility method
        self.__add(key, value, hash_key, self.hash_table)
        # adjust the table size and rehash if required
        load_factor = self.size / self.table_size
        if load_factor >= self.load_limit:
            self.resize(self.table_size * 2)

    def __add(self, key: Hashable, value: Any, hash_key: int, table: []) -> None:
        """
        Add utility function
        :param key: key
        :param value: value
        :param hash_key: hashed key
        :param table: table
        :return: None
        """
        # if table doesn't have this key
        if table[hash_key] is None:
            # create a new linkedlist and prepend the new key
            # value pair
            linked_list = ChainList()
            linked_list.prepend(key, value)
            table[hash_key] = linked_list
            self.size += 1
        # if the table has the key
        else:
            # get linkedlist at the location
            linked_list = table[hash_key]
            # check and update if the key is already present
            is_key_updated = linked_list.update_if_key_exists(key, value)
            # if not prepend the key, value
            if not is_key_updated:
                linked_list.prepend(key, value)
                self.size += 1

    def get(self, key: Hashable) -> Any:
        """
        Get the value corresponding to the key
        :param key: key
        :return: value
        """
        # Get the value of a key
        hash_key = self.hash_func(key) % self.table_size
        if self.hash_table[hash_key] is not None:
            return self.hash_table[hash_key].get(key)
        return None

    def remove(self, key: Hashable) -> None:
        """
        Remove an object from the hash table.
        :param key: the key to remove
        :return: None
        """
        # hashed key
        hash_key = self.hash_func(key) % self.table_size
        # if table contains key, remove it from linkedlist
        if self.contains(key):
            self.hash_table[hash_key].remove(key)
            self.size -= 1
        # If the linked list is becomes empty then removing it from the hash table
        if self.hash_table[hash_key] is not None and \
                self.hash_table[hash_key].front is None:
            self.hash_table[hash_key] = None
        # adjust size, it will rehash if required
        load_factor = self.size / self.table_size
        if load_factor < (1 - self.load_limit):
            self.resize(self.table_size // 2)

    def contains(self, key: Hashable) -> bool:
        """
        Check if key is contained in the hashmap
        :param key: key to be passed
        :return: boolean
        """
        # hashed key
        hash_key = self.hash_func(key) % self.table_size
        # check if the linked list at hash table is not None
        if self.hash_table[hash_key] is not None:
            return self.hash_table[hash_key].contains(key)
        return False

    def imbalance(self) -> float:
        """
        Computes the imbalance of the hashtable.
        :return: the average length of all non-empty chains minus 1, or 0 if hash table is empty
        """
        no_of_chains = 0
        no_of_elements = 0
        for cell in self.hash_table:
            if cell is not None:
                # no of elements in the linkedlist is going to be len(cell)
                # from the implemented __len__ method in ChainList
                no_of_elements += len(cell)
                no_of_chains += 1
        return 0 if no_of_elements == 0 else no_of_elements / no_of_chains - 1

    def resize(self, size) -> None:
        """
        Resize the table based on the given size value
        :param size: size
        :return: None
        """
        # You cannot resize less than the min buckets size
        size = max(size, self.MIN_BUCKETS)
        # new size comes out to be previous size then don't need to resize
        if size == self.table_size:
            return
        new_hash_table = [None] * size
        self.table_size = size
        self.size = 0
        # rehashing logic, iterating over all elements and adding
        # them to the new table
        for cell in self.hash_table:
            node = None if cell is None else cell.front
            while node is not None:
                hash_key = self.hash_func(node.key) % size
                self.__add(node.key, node.value, hash_key, new_hash_table)
                node = node.link
        self.hash_table = new_hash_table


def main():
    """
    Main method
    :return: None
    """
    hash_map = HashMap(hash_A)
    hash_map.add("2", 2)
    hash_map.add("3", 2)
    hash_map.add("4", 2)
    hash_map.add("4000", 4)
    for key, value in hash_map:
        print(key, value)
    print(hash_map.imbalance())


if __name__ == "__main__":
    main()

from LinkedNode import LinkedNode


"""
file:        MyStack.py
description: class to represent MyStack
language:    python3
author:      Abhijay Nair, an1147@rit.edu
author:      Sushruth Beeti, sb3112@rit.edu
"""


class MyStack:
    __slots__ = "top", "count"

    def __init__(self):
        """
        Constructor of MyStack
        """
        self.top = None
        self.count = 0

    def __str__(self):
        """
        To string method for MyStack
        :return: string of MyStack
        """
        s = "["
        n = self.top
        while n is not None:
            s += (str(n.value) + " ")
            n = n.link
        s += "]"
        return s

    def push(self, value) -> None:
        """
        Push an element in to the stack
        :param value: value
        :return: None
        """
        self.top = LinkedNode(value, self.top)
        self.count += 1

    def pop(self) -> None:
        """
        Remove an element from the stack
        :return: None
        """
        assert not self.is_empty(), "Pop from empty stack"
        self.top = self.top.link
        self.count -= 1

    def peek(self):
        """
        Get the top element from the stack
        :return: Top element of the stack
        """
        assert not self.is_empty(), "Pop from empty stack"
        return self.top.value

    def size(self):
        """
        Get size of the stack
        :return: size of the stack
        """
        return self.count

    def is_empty(self) -> bool:
        """
        Return boolean if stack is empty or not
        :return: boolean
        """
        return self.top is None

from LinkedNode import LinkedNode


"""
file:        MyQueue.py
description: class to represent MyQueue
language:    python3
author:      Abhijay Nair, an1147@rit.edu
author:      Sushruth Beeti, sb3112@rit.edu
"""


class MyQueue:
    __slots__ = "rear", "front", "count"

    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def __str__(self):
        """
        To string method for queue
        :return: string of my queue
        """
        s = "["
        n = self.front
        while n is not None:
            s += (str(n.value) + " ")
            n = n.link
        s += "]"
        return s

    def enqueue(self, value):
        """
        Enqueue the value in to the queue
        :param value: value
        :return: None
        """
        node = LinkedNode(value)
        if self.front is None:
            self.front = node
        else:
            self.rear.link = node
        self.rear = node
        self.count += 1

    def dequeue(self):
        """
        Remove the node from the front
        :return: None
        """
        assert not self.is_empty(), "Dequeue from empty queue"
        self.front = self.front.link
        if self.front is None:
            self.rear = None
        self.count -= 1

    def is_empty(self):
        """
        If the queue is empty
        :return: boolean
        """
        return self.front is None

    def peek(self):
        """
        Return the front element in the queue
        :return: Queue element
        """
        assert not self.is_empty(), "Peek from empty queue"
        return self.front

    def size(self):
        """
        The size of the queue
        :return: size
        """
        return self.count

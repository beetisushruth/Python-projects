"""
file:        LinkedNode.py
description: class to represent LinkedNode
language:    python3
author:      Abhijay Nair, an1147@rit.edu
author:      Sushruth Beeti, sb3112@rit.edu
"""


class LinkedNode:
    __slots__ = "value", "link"

    def __init__(self, value, link=None):
        """
        Constructor of the LinkedNode
        :param value: value of the linked node
        :param link: link of the linked node
        """
        self.value = value
        self.link = link

    def __str__(self):
        """
        To string method of linked node
        :return: string
        """
        return str(self.value)

    def __repr__(self):
        """
        Linked Node representation
        :return: linked node representation
        """
        return "LinkedNode(" + repr(self.value) + ", " + repr(self.link) + ")"

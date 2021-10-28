"""
file:        Passenger.py
description: class to represent passenger
language:    python3
author:      Abhijay Nair, an1147@rit.edu
author:      Sushruth Beeti, sb3112@rit.edu
"""


class Passenger:

    __slots__ = "name", "ticket_number", "has_carry_on"

    def __init__(self, name, ticket_number, has_carry_on):
        """
        Constructor method for passenger class
        :param name:            name of passenger
        :param ticket_number:   ticket number of the passenger
        :param has_carry_on:    has carry on
        """
        self.name = name
        self.ticket_number = ticket_number
        self.has_carry_on = has_carry_on

    def __str__(self):
        """
        To string method for passenger
        :return: to string method of passenger
        """
        return str(self.name + ', ticket: ' + self.ticket_number +
                   ', carry_on: ' + str(self.has_carry_on))
from MyQueue import MyQueue
from Passenger import Passenger

"""
file:        Gate.py
description: class to represent Gate
language:    python3
author:      Abhijay Nair, an1147@rit.edu
author:      Sushruth Beeti, sb3112@rit.edu
"""


class Gate:

    __slots__ = "boarding_queues", "gate_limit", "current_gate_count"

    def __init__(self, gate_limit, no_boarding_queues=4):
        """
        Constructor for gate class
        :param gate_limit:  gate limit
        :param no_boarding_queues:  number of boarding queues
        """
        self.boarding_queues = []
        for i in range(no_boarding_queues):
            self.boarding_queues.append(MyQueue())
        self.gate_limit = gate_limit
        self.current_gate_count = 0

    def enqueue_passenger(self, passenger: Passenger):
        """
        Enqueue the passenger
        :param passenger: passenger
        :return: boolean
        """
        ticket_number = passenger.ticket_number
        queue_no = int(ticket_number[0])
        if self.current_gate_count >= self.gate_limit:
            return False
        self.boarding_queues[queue_no - 1].enqueue(passenger)
        self.current_gate_count += 1
        return True

    def dequeue_passenger(self, queue_no: int):
        """
        Dequeue the passenger
        :param queue_no: queue number to pop the passenger from
        :return: None
        """
        if self.boarding_queues[queue_no].size() > 0:
            self.boarding_queues[queue_no].dequeue()
            self.current_gate_count -= 1

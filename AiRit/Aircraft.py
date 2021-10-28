from Gate import Gate
from MyStack import MyStack
from Passenger import Passenger

"""
file:        Aircraft.py
description: Class to represent aircraft
language:    python3
author:      Abhijay Nair, an1147@rit.edu
author:      Sushruth Beeti, sb3112@rit.edu
"""


class Aircraft:
    __slots__ = "passengers_with_carry_on", "passengers_without_carry_on", \
                "max_passengers_limit"

    def __init__(self, max_passengers_limit):
        """
        Constructor aircraft class
        :param max_passengers_limit:    maximum passengers limit
        """
        self.passengers_with_carry_on = MyStack()
        self.passengers_without_carry_on = MyStack()
        self.max_passengers_limit = max_passengers_limit

    def board_passenger(self, passenger: Passenger):
        """
        Board passenger into aircraft
        :param passenger: passenger
        :return:    boolean
        """
        if self.passengers_with_carry_on.size() + \
                self.passengers_without_carry_on.size() >= self.max_passengers_limit:
            return False
        if passenger.has_carry_on:
            self.passengers_with_carry_on.push(passenger)
        else:
            self.passengers_without_carry_on.push(passenger)
        return True

    def board_passengers(self, gate: Gate):
        """
        Board all passengers into aircraft
        :param gate:    gate
        :return:    None
        """
        is_aircraft_full = False
        if gate.current_gate_count > 0:
            print("Passengers are boarding the aircraft...")
        for i, queue in enumerate(gate.boarding_queues[::-1]):
            while queue.size() != 0:
                passenger = queue.peek().value
                has_passenger_boarded = self.board_passenger(passenger)
                if has_passenger_boarded:
                    print("\t" + str(passenger))
                    gate.dequeue_passenger(len(gate.boarding_queues) - i - 1)
                else:
                    print("The aircraft is full.")
                    is_aircraft_full = True
                    break
            if is_aircraft_full:
                break
        if not is_aircraft_full:
            print("There are no more passengers at the gate.")
        print("Ready for taking off ...")

    def disembark_passengers(self):
        """
        Disembark passengers from the aircraft
        :return:    None
        """
        if self.passengers_with_carry_on.size() + self.passengers_without_carry_on.size() > 0:
            print("The aircraft has landed.")
            print("Passengers are disembarking...")
        while self.passengers_without_carry_on.size() != 0:
            print("\t" + str(self.passengers_without_carry_on.peek()))
            self.passengers_without_carry_on.pop()
        while self.passengers_with_carry_on.size() != 0:
            print("\t" + str(self.passengers_with_carry_on.peek()))
            self.passengers_with_carry_on.pop()

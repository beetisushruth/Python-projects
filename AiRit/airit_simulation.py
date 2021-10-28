import sys

from Passenger import Passenger
from Aircraft import Aircraft
from Gate import Gate

"""
file:        airit_simulation.py
description: Python program to simulate adding passengers in line,
             boarding them and disembarking them
language:    python3
author:      Abhijay Nair, an1147@rit.edu
author:      Sushruth Beeti, sb3112@rit.edu
"""


def parse_file(file_name):
    """
    Parses the file and appends all the passenger details into a list
    :param file_name: name of the file
    :return: list of all passenger details
    """
    passenger_details = []
    try:
        with open(file_name) as f:
            for line in f:
                passenger_detail = line.strip().split(",")
                passenger_details.append(passenger_detail)
    except FileNotFoundError:
        print("File not found: ", file_name)
    except Exception:
        print("Error occurred while parsing file ", file_name)
    return passenger_details


def get_additional_details():
    """
    Gets additional details of fire-code mandated maximum
    number of passengers allowed at an airline gate and
    maximum passenger capcity of the aircraft
    :return: gate limit, max passenger capacity
    """
    gate_limit_message = "Gate capacity: "
    passenger_capacity_message = "Aircraft capacity: "
    gate_limit = input(gate_limit_message)
    while not gate_limit.isnumeric() or int(gate_limit) <= 0:
        print("Error: Fire code mandated gate limit entered must be a positive integer")
        gate_limit = input(gate_limit_message)
    max_passenger_capacity = input(passenger_capacity_message)
    while not max_passenger_capacity.isnumeric() or int(max_passenger_capacity) <= 0:
        print("Error: Maximum passenger capacity entered must be a positive integer")
        max_passenger_capacity = input(passenger_capacity_message)
    return int(gate_limit), int(max_passenger_capacity)


def enqueue_passengers_in_line(i, passenger_details, gate):
    print("Passengers are lining up at the gate...")
    while i < len(passenger_details) and gate.current_gate_count < gate.gate_limit:
        passenger_detail = passenger_details[i]
        # creating passenger object
        passenger = Passenger(passenger_detail[0], passenger_detail[1],
                              False if passenger_detail[2] == "False" else True)
        print("\t"+str(passenger))
        gate.enqueue_passenger(passenger)
        i += 1
    if gate.current_gate_count == gate.gate_limit:
        print("The gate is full; remaining passengers must wait.")
    return i


def start_simulation(passenger_details, gate_limit, max_passenger_capacity):
    """
    Start the lining up passengers at the gate and loading/unloading passengers to/from
    the aircraft
    :param passenger_details:  passenger details
    :param gate_limit:  fire-code mandated gate limit
    :param max_passenger_capacity:  maximum passsenger capacity
    :return: None
    """
    i = 0
    # gate object
    gate = Gate(gate_limit)
    # aircraft object
    aircraft = Aircraft(max_passenger_capacity)
    print("Beginning simulation...")
    while i < len(passenger_details):
        if gate.current_gate_count == 0:
            i = enqueue_passengers_in_line(i, passenger_details, gate)
        # passenger didn't enqueue which means the gate is full
        # now boarding passengers, take off and disembarking begins
        else:
            # board passengers in the aircraft
            aircraft.board_passengers(gate)
            # disembark passengers in the aircraft
            aircraft.disembark_passengers()
    # disembarking passengers one last time
    if gate.current_gate_count >= 0:
        print("The last passenger is in line!")
        aircraft.board_passengers(gate)
        aircraft.disembark_passengers()
    print("Simulation complete; all passengers are at their destination!")


def main():
    """
    Main method
    to parse command line arguments, load file
    and start the execution of program
    :return: None
    """
    arguments = sys.argv
    try:
        if len(arguments) > 2:
            raise ValueError("Too many command line arguments")
        file_name = arguments[1]
        passenger_details = parse_file(file_name)
        if len(passenger_details) > 0:
            gate_limit, max_passenger_capacity = get_additional_details()
            start_simulation(passenger_details, gate_limit, max_passenger_capacity)
    except (IndexError, ValueError) as e:
        print("Usage: python3 airit_simulation.py {filename}")


if __name__ == "__main__":
    main()

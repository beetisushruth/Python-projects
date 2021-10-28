from airit_simulation import *

"""
file:        airit_tests.py
description: Python program to test the airit_simulation.py methods
language:    python3
author:      Abhijay Nair, an1147@rit.edu
author:      Sushruth Beeti, sb3112@rit.edu
"""


def test_parse_file(test_cases):
    """
    Test the function parse file in airrit_simulation.py
    the function does parsing the passenger details from a given file
    If non existent file is provided it handles the exceptions and prints
    the relevant error message
    :return: None
    """
    for testcase in test_cases:
        passenger_details = parse_file(testcase[0])
        assert (len(passenger_details) == testcase[1]), "Testcase failed!"
        print("Test case passed for parsing the file '" + testcase[0] + "'")
        # printing out the passenger read from the file
        for passenger in passenger_details:
            print(passenger)


def test_get_additional_details(testcases):
    """
    Test the function load_additional_details which would basically
    take the input from the user for gate limit and max passenger capacity
    :param: testcases: test cases
    :return: None
    """
    for i in range(testcases):
        get_additional_details()
    print("All test cases successfully tested, code didn't break")


def test_enqueue_passengers_in_line(testcases):
    """
    Tests the function enqueue_passenger_in_line which would test how the
    enqueuing of the gate happens
    :param testcases: test cases
    :return: None
    """
    for testcase in testcases:
        i = enqueue_passengers_in_line(testcase["starting_passenger"],
                                       testcase["passengers"],
                                       testcase["gate"])
        assert(testcase["starting_passenger"] + testcase["expected"] == i), "Test case failed"


def test_start_simulation(testcases):
    """
    Tests the aircraft boarding and disembarking
    :param testcases: test cases
    :return: None
    """
    for testcase in testcases:
        start_simulation(testcase["passengers"],
                         testcase["gate_limit"],
                         testcase["max_passenger_capacity"])


def main():
    print("\nRUNNING TESTS FOR PARSE_FILE METHOD:")
    # These are the testcases for parsing file, filename and number of passengers
    # that are expected if the file was parsed
    test_cases_for_parse_file = [["ab.txt", 0],
                                 ["passengers_very_small.txt", 10],
                                 ["", 0],
                                 ["passengers_very_small.tx 23", 0]]
    test_parse_file(test_cases_for_parse_file)
    print("\nRUNNING TESTS FOR ENQUEUE_PASSENGERS_IN_LINE METHOD")
    # These are the testcases for enqueue_passengers_in_line method
    test_cases_for_enqueue_passengers = [{"gate": Gate(2), "passengers": [["Aaron", "200201", "False"],
                                                                          ["Michael", "200201", "False"],
                                                                          ["John", "300201", "False"],
                                                                          ["Mary", "100201", "False"]],
                                          "starting_passenger": 2,
                                          "expected": 2},
                                         {"gate": Gate(1), "passengers": [["Aaron", "200201", "False"],
                                                                          ["Michael", "200201", "False"]],
                                          "starting_passenger": 1,
                                          "expected": 1}]
    test_enqueue_passengers_in_line(test_cases_for_enqueue_passengers)
    print("RUNNING TESTS FOR START_SIMULATION METHOD")
    test_cases_for_start_simulation = [{"gate_limit": 2, "passengers": [["Aaron", "200201", "False"],
                                                                          ["Michael", "200201", "False"],
                                                                          ["John", "300201", "False"],
                                                                          ["Mary", "100201", "False"]],
                                        "max_passenger_capacity": 1,
                                        },
                                       {"gate_limit": 3, "passengers": [["Aaron", "200201", "False"],
                                                                          ["Michael", "200201", "False"],
                                                                          ["Mary", "100201", "False"]],
                                        "max_passenger_capacity": 4,
                                        }]
    test_start_simulation(test_cases_for_start_simulation)
    print("\nRUNNING TESTS FOR GET_ADDITIONAL_DETAILS METHOD")
    n = input("enter how many different gate_limit and max passenger limit "
              "you want to test? (valid positive integer): ")
    while not n.isnumeric() or int(n) <= 0:
        n = input("enter valid test case number: ")
    test_get_additional_details(int(n))


if __name__ == "__main__":
    main()

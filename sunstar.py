"""
file: sunstar.py
language: python3
description: Generates a sun star polygon with user entered parameters
author: Sushruth Beeti (sb3112@rit.edu)
author: Abhijay Nair (an1147@rit.edu)
"""

import turtle
import math


def init_turtle_environment(number_of_sides: int, length_of_side: int) -> None:
    """
    Initialize the turtle environment. Sets
    the environment dynamically according to length and number of sides
    :return: None
    """
    window_width = max(400, length_of_side * 4)
    window_height = max(400, length_of_side * 4)
    turtle.setup(window_width, window_height)
    turtle.setworldcoordinates(-window_width / 2, -window_height / 2,
                               window_width / 2, window_height / 2)
    tan_angle = math.tan(math.pi / number_of_sides)
    x_cor = -length_of_side / 2
    y_cor = 0 if number_of_sides == 1 or number_of_sides == 2 \
        else (length_of_side / (2 * tan_angle))
    turtle.penup()
    turtle.goto(x_cor, y_cor)
    turtle.setheading(0)
    turtle.speed(100)
    turtle.pendown()
    turtle.hideturtle()


def draw_side(length: float, levels: int, angle: int, side_length: float = 0) -> float:
    """
    Draws a single side of the sun star.
    :param side_length: length of the side
    :param length:  length of the side
    :param levels:  number of levels
    :param angle:   angle of deviation
    :return:        None
    """
    if levels == 1:
        turtle.forward(length)
        side_length += length
        return side_length
    else:
        turtle.forward(length / 4)
        side_length += (length / 4)
        turtle.left(angle)
        slant_length = (length / 4) / math.cos(angle * math.pi / 180)
        side_length = draw_side(slant_length, levels - 1, angle, side_length)
        turtle.right(2 * angle)
        side_length = draw_side(slant_length, levels - 1, angle, side_length)
        turtle.left(angle)
        turtle.forward(length / 4)
        side_length += (length / 4)
    return side_length


def draw_all_sides(number_of_sides: int, length: int,
                   levels: int, angle: int) -> None:
    """
    Draws all sides of a sun star
    :param number_of_sides: number of sides
    :param length:  length of the side
    :param levels:  number of levels
    :param angle:   angle of deviation
    :return:        None
    """
    total_side_length = 0.0
    interior_angle = ((number_of_sides - 2) * 180) / number_of_sides
    for i in range(number_of_sides):
        side_length = 0
        total_side_length += draw_side(length, levels, angle, side_length)
        turtle.right(180 - interior_angle)
    print('Total length is:', total_side_length)


def input_number_of_sides(message: str):
    """
    Input the number of sides. Negative number is converted to positive
    :param message: display message
    :return: number of sides
    """
    try:
        number_of_sides = abs(int(input(message)))
        if number_of_sides <= 0:
            print("Invalid number of sides provided. "
                  "Number of sides must be greater than 0")
        else:
            return number_of_sides
    except ValueError as error:
        print("Invalid number of sides provided. "
              "Excepted type 'int', provided 'string-value'")
    except Exception as exception:
        print("Invalid number of sides provided.")
    return input_number_of_sides(message)


def input_length_of_side(message):
    """
    Input the length of a side, negative value is converted to positive
    :param message: display message
    :return: number of sides
    """
    try:
        length_of_side = abs(int(input(message)))
        if length_of_side <= 0:
            print("Invalid length of side provided. "
                  "Length of side must be greater than 0")
        else:
            return length_of_side
    except ValueError as error:
        print("Invalid length of sides provided. Excepted type 'int', "
              "provided 'string-value'")
    except Exception as exception:
        print("Invalid length of sides provided.")
    return input_length_of_side(message)


def input_number_of_levels(message):
    """
    Input number of levels
    :param message: display message
    :return: levels
    """
    try:
        number_of_levels = int(input(message))
        if number_of_levels <= 0:
            print("Invalid number of levels provided. "
                  "Number of levels must be greater than 0")
        else:
            return number_of_levels
    except ValueError as error:
        print("Invalid number of levels provided. Excepted type 'int', "
              "provided 'string-value'")
    except Exception as exception:
        print("Invalid number of levels provided.")
    return input_number_of_levels(message)


def input_deviation_angle(message):
    """
    Input deviation angle
    :param message: display message
    :return: angle
    """
    try:
        angle = int(input(message))
        return angle
    except ValueError as error:
        print("Invalid deviation angle provided. Excepted type 'int', "
              "provided 'string-value'")
    except Exception as exception:
        print("Invalid deviation angle provided.")
    return input_deviation_angle(message)


def gather_input():
    """
    Gather input required to draw
    :return: number of sides, length of side, levels, angle
    """
    angle = 0
    number_of_sides = input_number_of_sides("Number of sides: ")
    length_of_side = input_length_of_side(
        "Length of initial side: ")
    number_of_levels = input_number_of_levels(
        "Number of levels: ")
    if number_of_levels > 1:
        angle = input_deviation_angle("Deflection angle: ")
    return number_of_sides, length_of_side, number_of_levels, angle


def main():
    """
    Main method to draw the sun star from user input
    :return:
    """
    number_of_sides, length_of_side, number_of_levels, angle = gather_input()
    init_turtle_environment(number_of_sides, length_of_side)
    draw_all_sides(number_of_sides, length_of_side, number_of_levels, angle)
    turtle.mainloop()


if __name__ == "__main__":
    main()

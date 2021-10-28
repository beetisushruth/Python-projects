"""
file: write_a_meme.py
description: Program writes a meme with the word 'TOM' using turtle library.
             Meme says: Tom ate a sauce, when you read fast, it sounds like
             Tomato Sauce.
language: python3
author: Sushruth Beeti, sb3112@rit.edu

"""

import turtle as t
import math

WINDOW_WIDTH = 850  # width of the canvas
WINDOW_HEIGHT = 400  # height of the canvas

LETTER_HEIGHT = 40  # letter height used
LETTER_WIDTH = 40  # letter width used
LETTER_SPACING = 20  # letter spacing used

RIGHT_ANGLE = 90  # largest angle in right angle triangle


def init() -> None:
    """
    Sets up the canvas and turtle for drawing
    (0, -100) is in the lower left and (850, 100) is in the upper right.
    :pre:  pos (0,0), heading (east), down
    :post: pos (0,0), heading (east), up
    """
    t.title("MEME ON TOM!")
    t.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    t.setworldcoordinates(0, -WINDOW_HEIGHT / 4, WINDOW_WIDTH, WINDOW_HEIGHT / 4)
    t.bgcolor("#b8fce7")
    t.pensize(5)
    t.setheading(0)
    t.speed(0)
    change_pen_state()
    t.hideturtle()


def draw_line(length):
    """
    Draws line with a required length
    :param length: how long the line should be drawn
    """
    t.forward(length)


def turn(angle, direction="right"):
    """
    Turn turtle by an angle and direction
    :param angle: angle to turn the turtle by
    :param direction: left or right direction
    """
    if direction == "left":
        t.left(angle)
    else:
        t.right(angle)


def change_pen_state(state="up"):
    """
    Changes pen state from up or down
    :param state: turtle's up or down writing state
    """
    if state == "up":
        t.up()
    else:
        t.down()


def draw_letter(letter):
    """
    Draw a letter
    :param letter: the letter to be drawn
    """
    if letter.lower() == "a":
        draw_letter_a()
    elif letter.lower() == 'c':
        draw_letter_c()
    elif letter.lower() == 'e':
        draw_letter_e()
    elif letter.lower() == 'm':
        draw_letter_m()
    elif letter.lower() == 'o':
        draw_letter_o()
    elif letter.lower() == 's':
        draw_letter_s()
    elif letter.lower() == "t":
        draw_letter_t()
    elif letter.lower() == 'u':
        draw_letter_u()
    else:
        default_space()


def draw_letter_a():
    """
    Draws letter 'A'
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    change_pen_state(state="down")
    turn(RIGHT_ANGLE, direction="left")
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_HEIGHT / 2)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    change_pen_state()
    turn(2 * RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    turn(RIGHT_ANGLE)
    change_pen_state(state="down")
    draw_line(LETTER_HEIGHT / 2)
    turn(RIGHT_ANGLE, direction="left")
    change_pen_state()


def draw_letter_c():
    """
    Draws letter 'C'
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    change_pen_state(state="down")
    turn(RIGHT_ANGLE, direction="left")
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    change_pen_state()
    turn(RIGHT_ANGLE)
    draw_line(LETTER_HEIGHT)
    change_pen_state(state="down")
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    turn(2 * RIGHT_ANGLE)
    change_pen_state()
    draw_line(LETTER_WIDTH)


def draw_letter_e():
    """
    Draws letter 'E'
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    turn(RIGHT_ANGLE, direction="left")
    change_pen_state(state="down")
    draw_line(LETTER_HEIGHT / 2)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    turn(2 * RIGHT_ANGLE)
    change_pen_state()
    draw_line(LETTER_WIDTH)
    turn(RIGHT_ANGLE)
    change_pen_state(state="down")
    draw_line(LETTER_HEIGHT / 2)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    change_pen_state()
    turn(RIGHT_ANGLE)
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE)
    change_pen_state(state="down")
    draw_line(LETTER_WIDTH)
    turn(2 * RIGHT_ANGLE)
    change_pen_state()
    draw_line(LETTER_WIDTH)


def draw_letter_m():
    """
    Draws letter 'M'
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    slant_length = math.sqrt(LETTER_HEIGHT ** 2 + (LETTER_WIDTH / 2) ** 2)
    angle = math.degrees(math.atan(LETTER_WIDTH / (2 * LETTER_HEIGHT)))
    turn(RIGHT_ANGLE, direction="left")
    change_pen_state(state="down")
    draw_line(LETTER_HEIGHT)
    turn(2 * RIGHT_ANGLE - angle)
    draw_line(slant_length)
    turn(2 * RIGHT_ANGLE - 2 * angle, direction="left")
    draw_line(slant_length)
    turn(2 * RIGHT_ANGLE - angle)
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE, direction="left")
    change_pen_state()


def draw_letter_o():
    """
    Draws letter 'O'
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    turn(RIGHT_ANGLE, direction="left")
    change_pen_state(state="down")
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    change_pen_state()
    turn(2 * RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)


def draw_letter_s():
    """
    Draws letter 'S'
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    change_pen_state(state="down")
    draw_line(LETTER_WIDTH)
    turn(RIGHT_ANGLE, direction="left")
    draw_line(LETTER_HEIGHT / 2)
    turn(RIGHT_ANGLE, direction="left")
    draw_line(LETTER_WIDTH)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_HEIGHT / 2)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    turn(RIGHT_ANGLE)
    change_pen_state()
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE, direction="left")


def draw_letter_t():
    """
    Draws letter 'T'
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    draw_line(LETTER_WIDTH / 2)
    change_pen_state(state="down")
    turn(RIGHT_ANGLE, direction="left")
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE, direction="left")
    draw_line(LETTER_WIDTH / 2)
    change_pen_state()
    turn(2 * RIGHT_ANGLE)
    draw_line(LETTER_WIDTH / 2)
    change_pen_state(state="down")
    draw_line(LETTER_WIDTH / 2)
    change_pen_state()
    turn(RIGHT_ANGLE)
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE, direction="left")


def draw_letter_u():
    """
    Draws letter 'U'
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    turn(RIGHT_ANGLE, direction="left")
    change_pen_state(state="down")
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE)
    change_pen_state()
    draw_line(LETTER_WIDTH)
    turn(RIGHT_ANGLE)
    change_pen_state(state="down")
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    change_pen_state()
    turn(2 * RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)


def draw_space():
    """
    Draws a space
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    draw_line(LETTER_WIDTH / 2)


def default_space():
    """
    Draws default space for every letter
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    draw_line(LETTER_SPACING)


def draw_tomato_body():
    """
    Draw a tomato body
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (west), up
    """
    change_pen_state(state="down")
    t.color("red")
    turn(RIGHT_ANGLE, direction="left")
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH)
    turn(RIGHT_ANGLE)
    change_pen_state()


def draw_tomato_leaf():
    """
    Draws tomato leaf
    :pre:  (relative to tomato body) pos (20,40), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    slant_length = math.sqrt((LETTER_HEIGHT / 4) ** 2 + (LETTER_WIDTH / 4) ** 2)
    angle = math.degrees(math.atan(1))
    t.color("green")
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH / 2)
    turn(RIGHT_ANGLE, direction="left")
    change_pen_state(state="down")
    draw_line(LETTER_HEIGHT / 2)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH / 8)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_HEIGHT / 8)
    turn(RIGHT_ANGLE, direction="left")
    draw_line(LETTER_HEIGHT / 4)
    turn(2 * RIGHT_ANGLE - angle)
    draw_line(slant_length)
    turn(RIGHT_ANGLE - angle, direction="left")
    draw_line(LETTER_HEIGHT / 8)
    turn(RIGHT_ANGLE)
    draw_line(LETTER_WIDTH / 8)
    change_pen_state()
    draw_line(LETTER_WIDTH / 2)
    turn(RIGHT_ANGLE, direction="left")
    draw_line(LETTER_HEIGHT)
    turn(RIGHT_ANGLE, direction="left")
    draw_line(LETTER_WIDTH)
    t.color("black")


def draw_tomato():
    """
    Draws a tomato
    :pre:  (relative) pos (0,0), heading (east), up
    :post: (relative) pos (LETTER_WIDTH,0), heading (east), up
    """
    draw_tomato_body()
    draw_tomato_leaf()


def draw_word(word):
    """
    Draws a word by drawing each letter
    :param word: the word to be drawn
    """
    for letter in word:
        draw_letter(letter)
        default_space()


def main():
    """
    Main method, initialises turtle environment and draws content
    """
    init()
    draw_word("Tom ate ")  # change the sentence here
    # available letters: t,o,m,a,e,s,u
    draw_tomato()
    draw_word(" sauce")
    t.done()


if __name__ == '__main__':
    main()

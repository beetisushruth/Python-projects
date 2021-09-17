"""
file: pigdice.py
language: python3
description: Holds a class for a pig dice game
author: Sushruth Beeti (sb3112@rit.edu)
author: Abhijay Nair (an1147@rit.edu)
"""

import turtle
import random
import score
import math


class PigDice:
    """
    Pigdice is a two player dice game using turtle library.
    Rules: First person to reach 50 points wins out of rolling dice.
           A player can roll a die any number of times he wants.
           The score gets added to his total score if he chooses to end
           his turn.
           If at any point a player rolls a one, no points are added.
    """

    right_angle = 90  # class variable common for all instances
    keeper = score.Keeper()  # score keeper instance

    def __init__(self: "PigDice", window_width=400, window_height=400,
                 dice_length=100, dot_size=10) -> None:
        self.window_width = window_width
        self.window_height = window_height
        self.dice_length = dice_length
        self.dot_size = dot_size
        self.win_score = 50

    def init_turtle_env(self: "PigDice") -> None:
        """
        Initialise turtle environment and pre-conditions
        :return: None
        """
        turtle.title("PIGDICE")
        turtle.setup(self.window_width, self.window_height)
        turtle.setworldcoordinates(-self.window_width / 4,
                                   -self.window_height / 4,
                                   self.window_width / 2,
                                   self.window_height / 2)
        turtle.pensize(5)
        turtle.setheading(0)
        turtle.speed(200)
        turtle.up()
        turtle.hideturtle()

    def draw_outline(self: "PigDice") -> None:
        """
        Draws dice outline
        :return: None
        """
        turtle.down()
        turtle.left(self.right_angle)
        for i in range(4):
            turtle.forward(self.dice_length)
            turtle.right(self.right_angle)
        turtle.right(self.right_angle)
        turtle.up()

    def draw_center_dot(self: "PigDice") -> None:
        """
        Draws center dot in the dice
        :return: None
        """
        hypotenuse = math.sqrt(self.dice_length ** 2
                               + self.dice_length ** 2)
        turtle.left(self.right_angle / 2)
        turtle.forward(hypotenuse / 2)
        turtle.dot(10)
        turtle.right(2 * self.right_angle)
        turtle.forward(hypotenuse / 2)
        turtle.left(1.5 * self.right_angle)
        turtle.up()

    def draw_two_dots(self: "PigDice") -> None:
        """
        Draws two dots in the dice
        :return: None
        """
        hyp = math.sqrt(self.dice_length ** 2
                        + self.dice_length ** 2)
        turtle.left(self.right_angle / 2)
        for i in range(1, 3):
            turtle.forward(i * (hyp / 4))
            turtle.down()
            turtle.dot(10)
            turtle.up()
        turtle.left(2 * self.right_angle)
        turtle.forward(0.75 * hyp)
        turtle.left(1.5 * self.right_angle)

    def draw_three_dots(self: "PigDice") -> None:
        """
        Draws three dots in the dice
        :return: None
        """
        self.draw_center_dot()
        self.draw_two_dots()

    def draw_four_dots(self: "PigDice") -> None:
        """
        Draws four dots in the dice
        :return: None
        """
        for i in range(0, 2):
            turtle.left(i * self.right_angle)
            turtle.forward(i * self.dice_length)
            turtle.right(2 * i * self.right_angle)
            self.draw_two_dots()
        turtle.forward(self.dice_length)
        turtle.left(self.right_angle)

    def draw_five_dots(self: "PigDice") -> None:
        """
        Draws five dots in the dice
        :return: None
        """
        self.draw_center_dot()
        self.draw_four_dots()

    def draw_dice(self: "PigDice", pips: int) -> None:
        """
        Draw the dice with the number of pips
        :param pips: number of dots to be drawn
        :return: None
        """
        assert 1 <= pips <= 5, "Illegal #pips: " + str(pips)
        if pips == 1:
            self.draw_center_dot()
        elif pips == 2:
            self.draw_two_dots()
        elif pips == 3:
            self.draw_three_dots()
        elif pips == 4:
            self.draw_four_dots()
        elif pips == 5:
            self.draw_five_dots()

    def refresh_dice(self: "PigDice") -> None:
        """
        Refresh the dice to clear the pips
        :return: None
        """
        turtle.color('black', 'white')
        turtle.begin_fill()
        turtle.down()
        for i in range(4):
            turtle.forward(self.dice_length)
            turtle.left(self.right_angle)
        turtle.end_fill()
        turtle.up()
        turtle.color('black')

    def draw_header(self: "PigDice") -> None:
        """
        Draws player scores header
        :return: None
        """
        turtle.left(2 * self.right_angle)
        turtle.forward(self.window_width / 4 + 10)
        turtle.right(self.right_angle)
        turtle.forward(0.40 * self.window_height)
        turtle.right(self.right_angle)
        turtle.down()
        turtle.color("black", "yellow")
        turtle.begin_fill()
        for i in range(4):
            if i % 2 == 0:
                turtle.forward(0.75 * self.window_width + 10)
            else:
                turtle.forward(45)
            turtle.left(self.right_angle)
        turtle.end_fill()
        turtle.up()
        turtle.home()

    def draw_current_score(self: "PigDice", current_score: int = 0) -> None:
        """
        Draws current score of the current player
        :param current_score: current score of a player
        :return: None
        """
        turtle.goto(10, 125)
        turtle.left(self.right_angle)
        turtle.color("white")
        turtle.begin_fill()
        for i in range(3):
            turtle.right(90)
            if i % 2 == 0:
                turtle.forward(100)
            else:
                turtle.forward(15)
        turtle.end_fill()
        turtle.color('black')
        turtle.write(f"Current Total = {current_score}",
                     font=('Arial', 14, 'normal'))
        turtle.up()
        turtle.home()

    def draw_player_scores(self: "PigDice", current_player: int = 1):
        """
        Draws the scores for two players
        :param current_player: current player that has finished playing
        :return: None
        """
        for i in range(0, 2):
            self.draw_player_score(i, current_player)

    def draw_player_score(self: "PigDice", player: int = 0, current_player: int = 0) -> None:
        """
        Draws player score in the header
        :param current_player: current player playing
        :param player: any player
        :return: None
        """
        if player == 0:
            turtle.goto(-90, 190)
        else:
            turtle.goto(90, 190)
        turtle.setheading(90)
        turtle.color('yellow')
        turtle.begin_fill()
        for i in range(3):
            turtle.right(90)
            if i % 2 == 0:
                turtle.forward(100)
            else:
                turtle.forward(15)
        turtle.end_fill()
        color = "black" if current_player == player else "blue"
        turtle.color(color)
        turtle.write(f"Player {player + 1} Total = "
                     f"{self.keeper.score[player]}",
                     font=('Arial', 14, 'normal'))
        turtle.color('black')
        turtle.penup()
        turtle.home()

    def draw_hold_button(self: "PigDice") -> None:
        """
        Draws the hold button
        :return: None
        """
        turtle.right(self.right_angle)
        turtle.forward(self.dice_length / 5)
        turtle.left(self.right_angle)
        turtle.down()
        turtle.color("black", "yellow")
        turtle.begin_fill()
        for i in range(0, 2):
            turtle.forward(self.dice_length)
            turtle.right(self.right_angle)
            turtle.forward((self.dice_length / 5))
            turtle.right(self.right_angle)
        turtle.end_fill()
        turtle.color("black")
        turtle.up()
        turtle.right(self.right_angle)
        turtle.forward(self.dice_length / 5)
        turtle.left(self.right_angle)
        turtle.forward(1 / 4 * self.dice_length)
        turtle.write("HOLD", font=("Verdana",
                                   20, "bold"))

        turtle.up()
        turtle.home()

    def draw_win_message(self: "PigDice", player: int) -> None:
        """
        Draws the win message
        :param player: current player
        :return: None
        """
        turtle.goto(15, -75)
        turtle.write(f"Player {player + 1} wins!!", font=('Arial', 14, 'normal'))

    def handle_click(self: "PigDice", x: float, y: float) -> None:
        """
        Handle on screen click
        :param x: x co-ordinate
        :param y: y co-ordinate
        :return: None
        """
        turtle_pos = turtle.pos()
        tx = int(turtle_pos[0])
        ty = int(turtle_pos[1])
        heading = turtle.heading()
        scores = self.keeper.score
        # case where a player has won already!
        if scores[0] >= self.win_score or scores[1] >= self.win_score:
            print("Game is finished!")
            return
        # to restrict asynchronous drawings on multiple clicks at once
        if not (tx == 0 and ty == 0 and heading == 0):
            print("Turtle is still drawing!")
            return
        buffer = -1.5
        # hold and dice limits
        hold_button_limits = [(0, -40), (self.dice_length, -20)]
        dice_limits = [(0, 0), (self.dice_length, self.dice_length)]
        # if click is inside hold button or dice
        if dice_limits[0][0] + buffer < x < dice_limits[1][0] - buffer and \
                dice_limits[0][1] + buffer < y < dice_limits[1][1] - buffer:
            self.handle_dice_click()
        if hold_button_limits[0][0] + buffer < x < hold_button_limits[1][0] - buffer and \
                hold_button_limits[0][1] + buffer < y < hold_button_limits[1][1] - buffer:
            self.handle_hold_click()

    def handle_dice_click(self: "PigDice") -> None:
        """
        Handle click the dice
        :return: None
        """
        pips = random.randint(1, 5)
        self.refresh_dice()
        self.draw_dice(pips)
        self.keeper.add_points(pips)
        self.draw_current_score(self.keeper.points)
        # when 1 is rolled, end case
        if pips == 1:
            self.draw_current_score(0)
            self.keeper.points = 0
            self.change_player()

    def handle_hold_click(self: "PigDice") -> None:
        """
        Handle click the hold button
        :return: None
        """
        if self.keeper.points == 0:
            return
        self.change_player()
        self.draw_current_score(0)
        self.refresh_dice()
        scores = self.keeper.score
        # output the win message
        if scores[0] >= self.win_score:
            self.draw_win_message(0)
        elif scores[1] >= self.win_score:
            self.draw_win_message(1)

    def change_player(self: "PigDice"):
        """
        Change player turns
        :return: None
        """
        self.keeper.switch_player()
        self.draw_player_scores(abs(self.keeper.player - 1))

    def start_game(self: "PigDice") -> None:
        """
        Start the pigdice game instance
        :return: None
        """
        self.init_turtle_env()  # init turtle
        self.draw_header()  # draw header for player scores
        self.draw_player_scores()
        self.draw_current_score()  # draw current score widget
        self.draw_outline()  # draw outline for dice
        self.draw_hold_button()  # draw hold button
        turtle.onscreenclick(self.handle_click)
        turtle.mainloop()


def run_game():
    """
    Method to run a pigdice game
    :return:
    """
    pig_dice = PigDice()
    pig_dice.start_game()


if __name__ == "__main__":
    run_game()

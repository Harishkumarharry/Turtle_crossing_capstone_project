from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)

    def display_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.level}", font=FONT)

    def next_level(self):
        self.level += 1
        self.display_scoreboard()

    def game_over_sequence(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=FONT)

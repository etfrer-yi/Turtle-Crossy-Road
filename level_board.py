from turtle import Turtle
BOARD_POSITION = (-380, 260)

class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(BOARD_POSITION)
        self.write(f"Level: {self.level}", font=("Arial", 16, "normal"))

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=("Arial", 16, "normal"))
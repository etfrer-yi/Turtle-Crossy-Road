from turtle import Turtle
UP_HEADING = 90
INITIAL_POSITION = (0, -275)
CAR_HALF_WIDTH = 40
CAR_HALF_HEIGHT = 20
FORWARD_PACE = 10

class Racer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(UP_HEADING)
        self.penup()
        self.goto(INITIAL_POSITION)

    def move_fwd(self):
        self.forward(FORWARD_PACE)

    def collision(self, cars):
        for car in cars:
            if car.ycor() + CAR_HALF_HEIGHT >= self.ycor() >= car.ycor() - CAR_HALF_HEIGHT \
                    and car.xcor() - CAR_HALF_WIDTH <= self.xcor() <= car.xcor() + CAR_HALF_WIDTH:
                return True





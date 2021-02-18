from turtle import Turtle
import random
SPEED_INCREMENT = 0.1
INITIAL_SPEED = 0.2


class Traffic(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = INITIAL_SPEED

    def color_car(self, car):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        car.color(R, G, B)

    def generate_car(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=3)
        car.setx(390)
        car.sety(random.randint(-200, 260))
        car.setheading(180)
        self.color_car(car)
        car.speed("slowest")
        self.cars.append(car)

    def generate_traffic(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def update_speed(self):
        self.car_speed += SPEED_INCREMENT

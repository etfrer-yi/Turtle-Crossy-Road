from turtle import Screen, Turtle
from racer import Racer, INITIAL_POSITION
from car import Traffic
from level_board import LevelBoard
import time

MS_IN_ONE_SEC = 1000
MS_INTERVAL = 500

screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.tracer(0)

racer = Racer()
traffic = Traffic()
level_board = LevelBoard()

screen.listen()
screen.onkey(racer.move_fwd, "Up")

initial_time =  round(time.time() * MS_IN_ONE_SEC)
game_over = False
while not game_over:
    screen.update()

    # Generate new cars every MS_INTERVAL milliseconds and maintain traffic
    if (round(time.time() * MS_IN_ONE_SEC) - initial_time) % MS_INTERVAL == 0:
        traffic.generate_car()
    traffic.generate_traffic()

    # Collision with a car
    if racer.collision(traffic.cars):
        game_over = True

    # Reaching the finish line and getting to next level
    if racer.ycor() >= 270:
        racer.goto(INITIAL_POSITION)
        traffic.update_speed()
        level_board.update_level()

screen.exitonclick()
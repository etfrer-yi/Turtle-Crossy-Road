from turtle import Turtle, Screen, ontimer
from racer import Racer, INITIAL_POSITION
from car import Traffic
from level_board import LevelBoard

MS_INTERVAL = 500

screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.tracer(0)

racer = Racer()
traffic = Traffic()
level_board = LevelBoard()
t = Turtle()
t.hideturtle()

screen.listen()
screen.onkey(racer.move_fwd, "Up")

def create_car():
    traffic.generate_car()
    screen.ontimer(create_car, t=MS_INTERVAL)

screen.ontimer(create_car, t=MS_INTERVAL)

game_over = False
while not game_over:
    screen.update()

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
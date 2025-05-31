import turtle

from turtle import Screen, Turtle
import random

tim = Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.speed(0)
        tim.right(size_of_gap)
        tim.circle(100)
draw_spirograph(5)

screen = Screen()
screen.exitonclick()
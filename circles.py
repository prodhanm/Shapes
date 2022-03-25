import turtle
import tkinter
from random import randint

turtle.bgcolor("white")

turtle.speed(0)
turtle.pensize(3)

colors = ["magenta", "cyan", "yellow", "white", "orange", "lightgreen"]

circles = 24
rad = 13
for i in range(circles):
    turtle.color(colors[randint(0, len(colors)-1)])
    turtle.circle(i*rad)

    turtle.penup()
    turtle.goto(0, -(i+1)*rad)
    turtle.pendown()
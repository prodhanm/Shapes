import turtle
import tkinter

turtle.speed(1)
turtle.color("red")
turtle.pensize(2)

for i in range(4):
    turtle.circle(80)
    for i in range(4):
        turtle.forward(250)
        turtle.left(90)
        turtle.goto(0, 50)
import turtle
import tkinter

turtle.bgcolor("black")

turtle.speed(0)
turtle.color("green")
turtle.pensize(4)

side = 500

turtle.penup()
turtle.goto(-side/2, -side/2)
turtle.pendown()

def spiral(side):
    for i in range(123):
        turtle.forward(side)
        turtle.left(90)
        side -= 4
    return side

spiral(side)
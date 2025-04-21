# Setup #
import turtle

t = turtle.Turtle()
t.penup()
t.goto(-100,50)
t.color("purple")
t.pendown()
t.speed(10)

# Code #
for i in range (2000):
    t.forward(300)
    t.left(171)
    t.forward(60)
    t.left(26)

# Ending #
turtle.exitonclick()
# Setup #
import turtle

t = turtle.Turtle()
t.color("cyan")
turtle.Screen().bgcolor("black")
t.speed(10)

# Code #
t.penup()
t.goto(-40, -10)
t.pendown()
for i in range (100):
    t.forward(100 + i)
    t.left(171)
    t.forward(20 + i)
    t.left(26)

t.color("gold")
t.setheading(0)
t.penup()
t.goto(-10, -230)
t.pendown()

for i in range (60):
    t.forward(30 + i/2)
    t.left(71)

t.penup()
t.goto(160, -160)
t.pendown()
for i in range (60):
    t.forward(30 + i/2)
    t.left(71)

t.penup()
t.goto(250, 0)
t.pendown()
for i in range (60):
    t.forward(30 + i/2)
    t.left(71)

t.penup()
t.goto(200, 160)
t.pendown()
for i in range (60):
    t.forward(30 + i/2)
    t.left(71)

t.penup()
t.goto(30, 210)
t.pendown()
for i in range (60):
    t.forward(30 + i/2)
    t.left(71)

t.penup()
t.goto(-170, 120)
t.pendown()
for i in range (60):
    t.forward(30 + i/2)
    t.left(71)

t.penup()
t.goto(-270, -30)
t.pendown()
for i in range (60):
    t.forward(30 + i/2)
    t.left(71)

t.penup()
t.goto(-200, -165)
t.pendown()
for i in range (60):
    t.forward(30 + i/2)
    t.left(71)


# Ending #
turtle.exitonclick()
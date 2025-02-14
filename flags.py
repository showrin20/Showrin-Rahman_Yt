
#Ukraine
from turtle import *
hideturtle()
speed(9)

color("gold")
begin_fill()
for i in range(2):
    forward(180)
    left(90)
    forward(50)
    left(90)
end_fill()

penup()
goto(0,50)
pendown()

color("blue")
begin_fill()
for i in range(2):
    forward(180)
    left(90)
    forward(50)
    left(90)
end_fill()


penup()
goto(-5,110)
pendown()
pensize(10)
color("black")
right(90)
forward(250)

#shape 2
import turtle
import math

draw = turtle.Turtle()
turtle.speed(10)
draw.hideturtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def leaf(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

for i in range(6):
        leaf(draw, 200, 360/6)
        draw.lt(360/6)
draw.lt(360/3)
turtle.penup()
arc(draw, 200, 360/6)
draw.lt(61)

circle(draw, 200)

turtle.mainloop()
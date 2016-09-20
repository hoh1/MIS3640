import turtle
import math

draw = turtle.Turtle()
turtle.speed(10)
draw.hideturtle()

def position (x,y):
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()

def polyline(t, n, length, angle):
    for i in range(n):
        turtle.fd(length)
        turtle.lt(angle)

def arc(t, r, angle, x, y):
    position(x, y)
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r, x, y):
    arc(t, r, 360, x, y)

#shape 3
def shape3(t, r, x, y):
    turtle.pensize(3)
    circle(draw, r, x, y-r)
    arc(draw, r/2, 180, x, y)
    arc(draw, r/2, 180, x, y)
    circle(draw, r/6, x, y+(r/3))
    circle(draw, r/6, x, y-(2*r/3))

shape3(draw, 100, 0, 0)


turtle.mainloop()
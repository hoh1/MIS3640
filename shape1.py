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

def bowtie(t, length):
    turtle.lt(30)
    for i in range(2):
        turtle.fd(length)
        turtle.rt(120)
    turtle.fd(length*2)
    for i in range(2):
        turtle.lt(120)
        turtle.fd(length)

def mirror_circle(t, r, x, y):
    circle(t, r, -x, -y)
    turtle.rt(180)
    circle(t, r, x, y)

def reset(rtangle): #reset the angle of the arrow
    turtle.setheading(0)
    turtle.rt(rtangle)


#shape 1

def shape_1(t, r):
    bowtie(draw, r)
    turtle.lt(60)
    bowtie(draw, r)
    turtle.rt(120)
    circle(draw, r, 0, -r)

    x = math.radians(60) # coordination of small circles
    y = math.sin(x)
    z = y * r

    a = math.radians(30) # radius of small circles
    b = math.cos(a)
    c = (r/4) / b

    mirror_circle(t, c, 0, z)
    reset(90)
    mirror_circle(t, c, z, 0)

shape_1(draw, 150)

turtle.mainloop()
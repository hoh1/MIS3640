import math

def quadratic(a,b,c):
    discriminant = (b**2)-(4*a*c)
    if discriminant < 0:
        print('This equation has no real solution')
    elif discriminant == 0:
        solution = -b / (2*a)
        print('There is 1 solution:', solution)
    else:
        solution1 = (-b + math.sqrt(discriminant)) / (2*a) 
        solution2 = (-b - math.sqrt(discriminant)) / (2*a) 
        print('There are 2 solutions:', solution1,'or', solution2)

a = float(input('Enter coefficient for a:'))
b = float(input('Enter coefficient for b:'))
c = float(input('Enter coefficient for c:'))
print(quadratic(a,b,c))

input()



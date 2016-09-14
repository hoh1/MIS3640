def my_abs(n):
    if isinstance(n, int) or isinstance(n, float):
        if n >= 0:
            return(n)
        else:
            return(-n)
    else:
        print('invalid value')

print(my_abs(100))

print(my_abs(0))

print(my_abs(-4))

print(my_abs('hello'))

input()
def sumall(*args):
    '''returns sum of all the arguments
    '''
    result = 0
    for number in args:
        result += number
    return result

print(sumall(1, 2, 3, 4, 5, 6, 7))
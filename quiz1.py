#Question 1:

def crazy_about_9(a, b):
    return a == 9 or b ==9 or a+b ==9 or abs(a-b) == 9

print(crazy_about_9(2, 9))
print(crazy_about_9(4, 5))
print(crazy_about_9(3, 8))

#Question 2:

def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False    
    elif year % 4 == 0:
        return True
    else:
        return False

print(leap_year(1900))
print(leap_year(2016))
print(leap_year(2017))
print(leap_year(2000))

#Question 3:

# Write a function with loops that computes The sum of all squares between 
# 1 and n (inclusive).

def sum_squares(n):
    result = 0
    for x in range(1, n+1):
        result += x*x
    return result
    
 
print(sum_squares(2))
print(sum_squares(100))

input()
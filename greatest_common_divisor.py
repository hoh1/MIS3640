'''
def gcd(a, b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(a, b % a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(a % b, b)  
'''
#Shortened Version
def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(a % b, b)  

a = int(input("Enter your 1st Number"))
b = int(input("Enter your 2nd Number"))
print(gcd(a, b))

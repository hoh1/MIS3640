# Exercise 5
# islower() -> returns TRUE 'only if'' all the letters are in lower case 
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# checks if the first letter of 'input' is in lower case;
# thus, returns true if the first letter is in lower case

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# returns true no matter what the letters are;

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
print(any_lowercase3('HeLLo'))
# returns TRUE only if the last last letter is in lower case 

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
print(any_lowercase4('HELLO'))
# returns false "only if" all the letters are in upper case
# otherwise, returns true

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
print(any_lowercase5('HELLO'))
# return FALSE if one of the letters is in upper case



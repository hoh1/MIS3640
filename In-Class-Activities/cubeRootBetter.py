x = int(input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))

# to-do
# make it work for negative integers.

# Below is the better version that works w/ negative integers
x = int(input('Enter an integer: '))
for g in range(abs(x+1)):
    if g**3 >= abs(x):
        break
if g**3 != abs(x):
     print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        g = -g
print('Cube root of ' + str(x) + ' is ' + str(g))












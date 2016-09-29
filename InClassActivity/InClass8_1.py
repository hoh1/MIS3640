import math
# Exercise 4: cheap is $33, free is $34 !
# part 1
def price(word):
    count = 0
    for letter in word:
        count += ord(letter)-96
    return count

print('bananas',  '$',price('bananas'))
print('rice',     '$',price('rice'))
print('paprika',  '$',price('paprika'))
print('potato chips',  '$',price('potato chips'))
print('-----------------')
print('Total',  '$', price('bananas')+price('rice')+price('paprika')+price('potato chips'))

# Modified Version from Part 1

print('{:18} {:1} {:6}'.format('bananas','$','52.00'))
print('{:18} {:1} {:6}'.format('rice',     '$','35.00'))
print('{:18} {:1} {:6}'.format('paprika',  '$','72.00'))
print('{:18} {:1} {:6}'.format('potato chips',  '$','78.00'))
print('--------------------------')
print('{:17} {:1} {:6}'.format('Total',  '$','237.00'))


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Big tiddle'
line2 = 'tiddle bang.'
#cat_twice(line1, line2)

#print(cat)
#print(cat_twice)

def give_me_a_break():
        str1 = 'break'
        print('another break')
        return str1
        

new_str = give_me_a_break()
print(new_str)

#print(give_me_a_break())

def a_new_function_demo():
    s = 0
    for x in 'chris':
        print(x)
        print(ord(x))
        s = s + ord(x)
    return s

print(a_new_function_demo())


input()
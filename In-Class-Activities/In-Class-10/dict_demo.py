names = ['Rose', 'Jerry', 'Alex']
scores = [95, 75, 85]
i = names.index('Jerry')
print(scores[names.index('Jerry')])

grades = {'Jerry': 75, 'Rose': 95}
print(grades['Jerry'])

grades['Brian'] = 90
print(grades)

print(len(grades))
print('Jerry' in grades)
print(90 in grades.values()) #in function is to see if '' exists inside the dictionary (returns TRUE/FALSE)


def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('Bookkeeper')
print(h)

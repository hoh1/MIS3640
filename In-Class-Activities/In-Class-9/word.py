fin = open('words.txt')
line = repr(fin.readline())
# https://docs.python.org/3/library/functions.html#repr

fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     print(word)

"""
prints only the words with more than 20 characters
"""
# def read_long_words():
#     for line in fin:
#         word = line.strip()
#         if len(word) > 20:
#             print(word)

# read_long_words() 
    
"""
returns True if the given word doesn’t have the letter “e” in it.
"""
# def has_no_e(word):
#     for letter in word:
#         if letter == 'e':
#             return False
#     return True

# print(has_no_e('Babson'))
# print(has_no_e('College'))

"""
takes a word and a string of forbidden letters, and that returns True
if the word doesn’t use any of the forbidden letters.
"""
# def avoids(word, forbidden):
#     for letter in word:
#         if letter in forbidden:
#             return False
#         else:
#             return True

# print(avoids('Babson','ab'))
# print(avoids('College','ab'))
"""
takes a word and a string of letters, and that returns True if the word
contains only letters in the list.
"""
# def uses_only(word, available):
#     for letter in word:
#         if letter not in available:
#             return False
#         return True

# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college','aBbsonxyz'))

"""
takes a word and a string of required letters, and that returns True if
the word uses all the required letters at least once.
"""
# def uses_all(word, required):
#     for letter in required:
#         if letter not in word:
#             return False
#         return True

# Or, we can use previously built function to make it simpler
# return uses_only(required,word)

# print(uses_all('Babson', 'abs'))
# print(uses_all('College', 'abs'))

"""
returns True if the letters in a word appear in alphabetical order
(double letters are ok).
"""
def is_abecedarian(word):
    before = word[0]   #this represents the 1st letter
    for letter in word:
        if letter < before:
            return False
        before = letter
    return True

print(is_abecedarian('abs'))
print(is_abecedarian('college'))

# Rewrite Using While Loop

def is_abecedarian(word):
    count = 0
    while count < len(word)-1:
        if word[count] > word[count+1]:
            return False
        count += 1
    return True
print(is_abecedarian('abs'))
print(is_abecedarian('college'))


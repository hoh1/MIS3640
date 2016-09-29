# Exercise 3
"""
Tests if a word contains three consecutive double letters.
word: string
returns: bool
"""
def is_triple_double(word):
    for i in range(len(word)-5):
        if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
            return True            
    return False
        
       
print(is_triple_double('hello'))
print(is_triple_double('mississippi'))
print(is_triple_double('aabbcc'))


def find_triple_double():
    """
    Reads a word list and prints words with triple double letters.
    """
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')

def rotate_world(word, n):
    result = str()
    for letter in word:
        if ord(letter) >= 122:
            result += chr(96 + n)
        else:
            result += chr(ord(letter) + n)
    return result
    
print(rotate_world('cheer', 7))
print(rotate_world('zybcd', 1))
print(rotate_world('ibm', -1))

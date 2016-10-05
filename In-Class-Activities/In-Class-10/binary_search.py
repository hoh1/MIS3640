test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()
def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''
    high = len(my_list) - 1
    low = 0
    while True:
        if x in my_list:
            index = int((high + low) / 2.0)
            if my_list[index] < x:
                low = index + 1
            if my_list[index] > x:
                high = index - 1
            if my_list[index] == x:
                return index
        else:
            return None
      
                  
        
print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None

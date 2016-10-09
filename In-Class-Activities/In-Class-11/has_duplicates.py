dup_list = [3, 5, 7, 9, 9, 1]
 
def has_duplicates(dup_list):
   dictionary = {}
   for item in dup_list:
       dictionary[item] = 1 + dictionary.get(item, 0)
       if dictionary[item] > 1:
           return True
   return dup_list
 
print(has_duplicates(dup_list))
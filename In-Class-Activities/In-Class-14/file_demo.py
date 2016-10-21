import os
cwd = os.getcwd()

# fout = open('output.txt', 'w') #'w' for write, as 'r' is for read;

# line_1 = "How many roads must a man walk down\n"   #'\n' is to jump the line(=enter)
# fout.write(line_1)

# line_2 = "Before you call him a man?\n"
# fout.write(line_2)

# fout.close()  #make sure to close the file!

# print(os.path.exists('output.txt')) #test whether the file exists
# print(os.path.isdir('exercises')) # isdir => folder name

# # Exercise 1
# def walk2(dirname):  #count the number of files in current working directory, and their names;
#     """Prints the names of all files in 
#     dirname and its subdirectories.

#     dirname: string name of directory
#     """
#     count = 0
#     for root, dirs, files in os.walk(dirname):
#         for filename in files:
#             print(os.path.join(root, filename))
#             count += 1
#     print(count, 'files in total.')

# walk2(os.getcwd())

#Exercise 2

try:    
    fin = open('bad_file')
except:
    print('Something went wrong.')

print('still works here.')





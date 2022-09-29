# Zachary Smith
# PA_7

import random

try:
    # read file path
    str1 = input("Enter the path to the file you wish to create:")
    # read file name
    str2 = input("Enter the file name:")
    if str1[len(str1) - 1] == '\\':
        str1 = str1 + str2
    else:
        str1 = str1 + '\\' + str2
    f = open(str1, "w")  # open the file in write mode
    for i in range(50):  # generate 50 random numbers and write into file
        f.write(str(random.randint(1, 1000)) + "\n")
    f.close()  # close the file
    print("The 50 random numbers have been written to the file successfully.")
except (IOError, PermissionError):
    print("You do not have permission to access the folder")
    print("The program has ended")

try:
    str1 = input("Enter the path to the file you wish to read:")
    str2 = input("Enter the file name:")
    if str1[len(str1) - 1] == '\\':
        str1 = str1 + str2
    else:
        str1 = str1 + '\\' + str2
    # open the file in read mode
    f = open(str1)
    # read file inform of lines
    l = f.readlines()
    l = list(map(int, l))
    print("The lowest number is:", min(l))
    print("The highest number is:", max(l))
    print("The sum of the numbers in the list is:", sum(l))
    print("The average of the numbers in the list is:", sum(l) / len(l))
except (FileNotFoundError, IOError):
    print("The", str1, "does not exist")
    print("The program has ended")
print("The 50 random numbers have been written to the file successfully")

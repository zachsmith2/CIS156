# Zachary Smith
# PA_4

import random
random_lst = []
# random integer from -100 to 100
for i in range(0, 20): # setting range to 20 numbers
    random_lst.append(random.randint(-100, 100))
print('The list contains: ', random_lst) # Printing the randomly generated numbers in a list
# setting the base values to 0
lowest = random_lst[0]
highest = random_lst[0]
total = 0
for num in random_lst:
    if num < lowest:
        lowest = num     # The lowest number
    if num > highest:
        highest = num    # The highest number
    total += num       # The total is adding up all of the numbers
# Printing the statements and setting the values to the according statements
print('The lowest number is:' + str(lowest))
print('The highest number is: ' + str(highest))
print('The sum of the numbers is: ' + str(total))
print('The average of the numbers in the list is: ' + str(total/len(random_lst)))

# Zachary Smith
# PA_3
# This program calculates the surface area of a python
from math import sqrt


def calculate_area(l, w, h):  # defining function
    result = (l * w) + l * sqrt((w / 2) ** 2 + h ** 2) + w * sqrt(
        (l / 2) ** 2 + h ** 2)  # calculating surface area of # right rectangular pyramid
    return result


# get the inputs from the user
length = float(input("Enter the pyramid's length: "))
width = float(input("Enter the pyramid's width : "))
height = float(input("Enter the pyramid's height : "))

A = calculate_area(length, width, height)  # Call in function with users added inputs
print("The surface area of the right rectangular pyramid is: ", format(A, '.2f'))  # calling the function with 2
# decimal places

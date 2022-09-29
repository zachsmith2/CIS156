# Zachary Smith
# PA_5
# checking a knowledge on the basis of score
def display_results(c):
    print("You got", c, "questions correct.")
    # if number of correct answers is >=8
    if c >= 8:
        print("Your knowledge of largest cities is great!!")

    # if number of correct answers is >=6
    elif c >= 6:
        print("Your knowledge of largest cities is above average!")

    # if number of correct answers is >=4
    elif c >= 4:
        print("Your knowledge of largest cities is average.")

    # if number of correct answers is <4
    elif c < 4:
        print("You better study more!!!")


# Dictionary with the state and largest city

largest_City = {
    'North Dakota': 'Fargo',
    'South Dakota': 'Sioux Falls',
    'Nebraska': 'Omaha',
    'Kansas': 'Wichita',
    'Oklahoma': 'Oklahoma City',
    'Texas': 'Houston',
    'Minnesota': 'Minneapolis',
    'Iowa': 'Des Moines',
    'Missouri': 'Kansas City',
    'Arkansas': 'Little Rock',
}

# initial count of correct answers
c = 0

# loop through dictionary
for i in largest_City:

    # ask the user ti enter the city capital
    print("What is the largest city in", i, end=": ")

    # get input
    t = input()

    # if answer is correct
    # print appropriate message and
    # increase the count
    if t == largest_City[i]:
        print("You are CORRECT,", largest_City[i], "is the largest city in", i)
        c = c + 1

    # else print appropriate message
    else:
        print("You are INCORRECT,", largest_City[i], "is the largest city in", i)

    print()
# call the display result function by passing c
display_results(c)

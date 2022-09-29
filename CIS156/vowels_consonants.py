# Zachary Smith
# PA_6

def count_vowels(string):
    count = 0
    for x in string:
        if x.isalpha():
            if x in "AEIOUaeiou":
                count += 1
    return count


def count_consonants(string):
    count = 0
    for x in string:
        if x.isalpha():
            if not x in "AEIOUaeiou":
                count += 1
    return count


s = input("Enter a string: ")
print("The string you entered includes", count_vowels(s), "vowels and", count_consonants(s), "consonants.")

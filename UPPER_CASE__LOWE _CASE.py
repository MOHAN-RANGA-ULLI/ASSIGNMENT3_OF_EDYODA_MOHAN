# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def count_characters(string):
    upper_case_char = 0
    lower_case_char = 0

    for char in string:

        if char.isupper():
            upper_case_char = upper_case_char + 1
        elif char.islower():
            lower_case_char = lower_case_char + 1
    return upper_case_char , lower_case_char

string1 = input('enter the string:')

upper , lower = count_characters(string1)

print("No. of Upper case characters:", upper)
print("No. of Lower case characters:", lower)


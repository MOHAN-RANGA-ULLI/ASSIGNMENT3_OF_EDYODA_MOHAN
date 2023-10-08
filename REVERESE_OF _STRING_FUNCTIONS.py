def reverse_of_string(input_string):

    string = ''

    for char in input_string:
        string = char + string
    return string

string1 = input('enter the string :')
result = reverse_of_string(string1)
print('the reverse of a string:' , result)


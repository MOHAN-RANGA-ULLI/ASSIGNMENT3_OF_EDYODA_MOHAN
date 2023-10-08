def sum_of_list(list):

    sum=0
    for i in list:
        sum = sum +i
        
    return sum

l=eval(input('enter the elements of the list :'))
print('sum of all elements present ina list:' , sum_of_list(l))
'''
Createa function called biggest_odd that takes a string of
numbers as an argument and returns the biggest odd number in the
string. For example, if you pass ‘23569’ as an argument, your
function should return 9. Use list comprehension.

'''

def biggest_odd(str):
    my_list = []
    for i in str:
        my_list.append(i)
    return print(max(my_list))
    
biggest_odd('23569')

'''
Write a function called zeros_last. This function takes a list as an
argument. If a list has zeros (0), it will move them to the end of the
list and maintain the order of the other numbers in the list. If there
are no zeros in the list, the function should return the original list,
sorted in ascending order. For example, if you pass [1, 4, 6, 0, 7, 0,9]
as an argument, your code should return [1, 4, 6, 9, 0, 0]. If
you pass [2, 1, 4, 7, 6] as your argument, your code should return
[1, 2, 4, 6, 7].

'''

def zeros_last(lst):
        
    for i in lst:
        if i == 0:
            lst.remove(0)
            lst.append(0)
    
    return print(lst)
           
    
    
zeros_last([1, 4, 6, 0, 7, 0,9])
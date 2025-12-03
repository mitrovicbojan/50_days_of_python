'''
Write a function called any_number that can receive any
number of positional arguments (integers and floats) and return
the average of those integers. If you pass 12, 90, 12 and 34 as
arguments, your function should return 37.0 as the average. If you
pass 12 and 90, your function should return 51.0 as the average.

'''
def any_number(*args):
    list_of_nums = list(args)
    
    list_sum = sum(list_of_nums)
    
    return print(list_sum / len(list_of_nums))

any_number(12,90)
'''
Write a function called add_reverse. This function takes two
lists as arguments, adds each corresponding number, and
reverses the outcome. For example, if you pass [10, 12, 34]
and [12, 56, 78], your code should return [112, 22, 68]. If the
two lists are not of equal length, the code should return a
message that "the lists are not of equal length.
"
'''

def add_reverse(lst, lst2):
    if len(lst) != len(lst2):
        return "The lists are not of equal length."
    
    reversed_list = []    
    count = 0  
   
    for i in lst:
        reversed_list.append(i + lst2[count])            
        count=count + 1 
      
    return list(reversed(reversed_list))

    

print(add_reverse([10, 12, 34], [12, 56, 78]))
'''
Write a function called odd_even that has one parameter and
takes a list of numbers as an argument. The function returns the
difference between the largest even number in the list and the
smallest odd number in the list. For example, if you pass [1, 2,
4, 6] as an argument, the function should return 6 - 1= 5.

'''

def odd_even(num_lst):
    max_even_num = 0
    min_odd_num = 0
    if max(num_lst) % 2 == 0:
        max_even_num = max(num_lst)  
          
    if min(num_lst) % 2 == 1:
        min_odd_num = min(num_lst) 
        
    return max_even_num - min_odd_num
     
     
print(odd_even([1, 2,4, 6]))

'''
Write a function called prime_numbers. This function asks the
user to enter a number (an integer) as an argument and returns a
list of all the prime numbers within its range. For example, if the
user enters 10, your code should return [2, 3, 5, 7] as prime
numbers.
'''
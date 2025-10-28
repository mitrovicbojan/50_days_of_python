'''
Write a function called divide_or_square that takes one
argument (a number) and returns the square root of the number if
it is divisible by 5, or its remainder if it is not divisible by 5. For
example, if you pass 10 as an argument, then your function should
return 3.16 as the square root.

'''

def divide_or_square(num):
    if num % 5 == 0:
        sq_root = num ** 0.5
        return f"The square root of {num} is {sq_root}."
    else: 
        remainder = num % 5
        return f"{num} is not divisible by 5, and its remainder is {remainder}."
     
result = divide_or_square(10)
print(result)

'''
Write a function called longest_value that takes a dictionary as
an argument and returns the first longest value of the dictionary.
For example, the following dictionary should return "apple" as the
longest value.
fruits = {'fruit': 'apple','color': 'green'}
'''

def longest_value(dict):
    max_length = -1
    max_val = None
    
    for value in dict.values():
        if len(value) > max_length:
            max_length = len(value)
            max_val = value
    return f"The first longest value of the dictionary is: {max_val}."

fruits = {'fruit': 'apple','color': 'green'}

result_longest_value = longest_value(fruits)

print(result_longest_value)
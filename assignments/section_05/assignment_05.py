'''
Write the logic that determines if a number meets specific range criteria. 
This exercise helps you practice conditional logic and multiple condition
checking in Python.

Instructions

Create a function called range_checker that accepts 3 parameters: 
number, min_val, and max_val

Return True if the number satisfies ANY of the following conditions:

The number is within the range [min_val, max_val] (inclusive), OR

The number is exactly double the min_val, OR

The number is exactly half the max_val

Return False otherwise

Sample Output

range_checker(5, 1, 10)   # Returns: True (5 is within range 1-10)
range_checker(15, 5, 12)  # Returns: False (15 is not in range, not double 5, not half of 12)
range_checker(10, 5, 12)  # Returns: True (10 is double of min_val 5)
range_checker(6, 4, 12)   # Returns: True (6 is half of max_val 12)
'''

def range_checker(number, min_val, max_val):
    dbl_min_val = min_val * 2
    half_max_val = max_val / 2
    
    if (number <= max_val and number >= min_val) or (number == dbl_min_val) or (number == half_max_val):
        return True
    else:
        return False

print(range_checker(15, 5, 12))
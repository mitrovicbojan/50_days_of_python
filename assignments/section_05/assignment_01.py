'''
Even or Odd?
Write a function even_or_odd(n) that returns the string 
'Even' if the integer n is even, and 'Odd' if n is odd.

Requirements

The function should take a single integer argument.

Return 'Even' if the number is even, 'Odd' if the number is odd.

Use an if/else statement for the logic.
'''

def even_or_odd(n):
    result = n % 2
    if result == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(12))
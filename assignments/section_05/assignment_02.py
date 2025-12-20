'''
Sum of N Natural Numbers
Write two functions, sum_with_for(n) and sum_with_while(n), 
that each return the sum of all numbers from 1 to n (inclusive). 
First function should use the for loop, 
and the Second function should use the while loop.

Requirements

sum_with_for(n): Use a for loop to sum numbers from 1 to n.

sum_with_while(n): Use a while loop to sum numbers from 1 to n.

Both functions should return the sum as an integer.

Assume n >= 1.

'''
def sum_with_for(n):
    result = 0   
    for i in range(1, n +1):
         result +=i
    return result

def sum_with_while(n):
    result = 0
    i = 1
    while i < n + 1: 
        result +=i      
        i +=1
    return result

print("for loop result")
print(sum_with_for(10))
print("while loop result")
print(sum_with_while(10))
''' 
You should define a function named square_root_bisection with three parameters:

The number for which you want to find the square root.
The tolerance being the acceptable error margin for the result.
You should set a default tolerance value.
The maximum number of iterations to perform. 
You should set a default number of iterations.
The square_root_bisection function should:

Raise a ValueError with the message 
Square root of negative number is not defined in real numbers 
if the number passed to the function is negative.
For numbers 0 and 1, print the message: 
The square root of [number] is [number] and return 
the number itself as the square root.
For any other positive number, print the approximate 
square root with the message: The square root of [square_target] 
is approximately [root] and return the computed root value.
If no value meets the tolerance condition, 
print a failure message: 
Failed to converge within [maximum] iterations and return None.
'''

def square_root_bisection(num, tolerance=0.001, iterations=100):
    if num < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    if num == 1 or num == 0:
        print(f"The square root of {num} is {num}")
        return num
    
   
    if num >= 1:
        lower = 0
        upper = num
    elif 0 < num < 1:
        lower = 0
        upper = 1
         
    for i in range (iterations):
        mid = (lower + upper)/2
        square = mid * mid
        if (upper - lower)/2 < tolerance:
            mid = (lower + upper)/2
            print(f"The square root of {num} is approximately {mid}")
            return mid
        
        if square < num:
            lower = mid
        else:
            upper = mid
    
    print(f"Failed to converge within {iterations} iterations")
    return None    

square_root_bisection(0.001, 1e-7, 50)
        
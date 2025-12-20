'''
Personal Info Management 1

Problem Statement
Write a function create_person(*args) that manages personal details. 
This function should accept a variable number of arguments using *args 
and return a dictionary containing the personal details. 
The function should be flexible, allowing for one, two, 
or three positional arguments.

Function Requirements

If one argument is passed, the function should return a dictionary 
containing the name attribute.

If two arguments are passed, the function should return a dictionary 
containing both name and age.

If three arguments are passed, the function should return a dictionary 
containing name, age, and address.

If the number of arguments passed is not one, two, or three, 
the function should raise an IndexError.
'''
def create_person(*args):
    
    key_lst = ["name", "age", "address"]
    if len(args) > 3:
        raise IndexError("You added too many arguments")
    else:
        result = dict(zip(key_lst, args))
        return result
    
   
    
print(create_person("tom"))
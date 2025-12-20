'''
Write a function create_person_with_details(*args, **kwargs) that manages personal details. 
This function should accept a variable number of positional arguments 
using *args and keyword arguments using **kwargs. 
The function should return a dictionary containing the personal details.

Function Requirements

If one positional argument is passed, 
the function should return a dictionary containing only the name attribute.

If two positional arguments are passed, 
the function should return a dictionary containing both name and age.

If three positional arguments are passed, 
the function should return a dictionary containing name, age, and address.

The function should also handle keyword arguments (**kwargs), 
allowing additional details like phone_number to be added to the dictionary.

If the number of positional arguments passed is not one, two, or three, 
the function should raise an IndexError.

'''

def create_person_with_details(*args, **kwargs):
    keys = ["name", "age", "address"]

    if len(args) < 1 or len(args) > 3:
        raise IndexError("Function accepts only 1, 2, or 3 positional arguments")

    person = dict(zip(keys, args))
    
    person.update(kwargs)

    return person

print(create_person_with_details("tom", 55, "NYC"))
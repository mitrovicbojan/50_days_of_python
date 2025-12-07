# Assignment 2

"""
Create a method called pay_extra that accepts 2 parameters:
 working, and hour. This method will be used to decide whether
 an employee will receive extra pay or not. If an employee is working
 during the hrs of 8pm until 8am in the morning, that means they
 should be paid extra. In that situation the method should return true,
 otherwise it should return false.

 NOTE: the hour parameter should be from 0-23.
        So 8AM is hour 8, and 8PM is hour 20.

Example:
    pay_extra(True, 11) -> false
    pay_extra(False, 5) -> false
    pay_extra(True, 6)  -> true
"""

# Your Code Below:

def pay_extra(working, hours):
    
    extra_hours = [21,22,23,24,1,2,3,4,5,6,7]
    working_extra_hours = False
    
    for i in extra_hours:
        if i == hours:
            working_extra_hours = True
    
    if  working == True and working_extra_hours == True:
        return "true"
    
    return "false"

print(pay_extra(True, 8))


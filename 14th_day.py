'''
Writea function called flat_list that takes one argument, a nested
list. The function converts the nested list into a one-dimensional
list. For example, [[2, 4, 5, 6]] should return [2, 4, 5, 6].
'''

def flat_list(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flat_list(item)
        else:
            yield item

flat = list(flat_list([[2, 4, 5, 6]]))

print(flat)

'''
A school has asked you to write a program that will calculate
teachers' salaries. The program should ask the user to enter the
teacher’s name, the number of periods taught in a month, and
the rate per period. The monthly salary is calculated by
multiplying the number of periods by the monthly rate. The
current monthly rate per period is $20. If a teacher has more than
100 periods in a month, everything above 100 is overtime.
Overtime is $25 per period. For example, if a teacher has taught
105 periods, their gross monthly salary should be $2,125. Write a
function called "your_salary" that calculates a teacher’s gross
salary. The function should return the teacher’s name, periods
taught, and gross salary. Here is how you should format your
output: Teacher: John Kelly, Periods: 105 Gross salary:2,125
'''

def your_salary():
    name_input = input("Enter your full name: ")
    classes_input = int(input("Enter the number of periods taught in a month: "))
    rate_input = int(input("Enter the rate per period: "))
    
    overtime_pay = 25
    
    extra_lessons = classes_input - 100
    
    if extra_lessons > 0:
        return f"{name_input}, Periods: {classes_input}, Gross salaray: {(classes_input - extra_lessons) * rate_input + (extra_lessons * overtime_pay)}"
    else:
        return f"{name_input}, Periods: {classes_input}, Gross salaray: {classes_input * rate_input}"
    
   
print(your_salary())
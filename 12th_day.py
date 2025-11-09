'''
Write af unction called count_dots. This function takes a string
separated by dots as a parameter and counts how many dots are in
the string. For example,
"h.e.l.p." should return 4 dots, and
"he.lp." should return 2 dots.
'''

def count_dots(my_str):
    dots = 0
    for i in my_str:
        if i == '.':
            dots = dots + 1
    return dots

print(count_dots("he.lp."))
            
            
'''
Write a function called age_in_minutes that tells a user how
old they are in minutes. Your code should ask the user to enter
their year of birth, and it should return their age in minutes (by
subtracting their year of birth from the current year). Here are
things to look out for:
a. The user can only input a 4-digit year of birth. For example,
1930 is a valid year. However, entering any number longer
or shorter than 4 digits, should render the input invalid.
Notify the user that they must enter a four-digit number.
b. If a user enters a year before 1900, your code should tell
the user that the input is invalid. If the user enters the year
after the current year, the code should tell the user to input
a valid year.
The code should run until the user inputs a valid year. Your
function should return the user's age in minutes. For example, if
someone enters 1930 as their year of birth, your function should
return:
You are 48, 355, 200 minutes old.
'''
#A standard year has 525,600 minutes, while a leap year has 527,040 minutes
from datetime import date
import calendar
#calendar.isleap()

d = date.today().year

user_year = 1945

min_old = 0

for i in range(user_year, d):
    if calendar.isleap(user_year):
        min_old = min_old + 527040
    else: 
        min_old = min_old + 525600

print(f"{min_old:,}")
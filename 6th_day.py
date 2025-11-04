'''
Write a function called user_name that generates a username
from the user's email. The code should ask the user to input an
email, and the code should return everything before the @ sign
as their user name. For example, if someone enters
ben@gmail.com, the code should return ben as their user
name.
'''

def user_name():
    user_email = input("Enter your email: ")
    acc_name = user_email.strip("?@")
    return f"Your user name is: {acc_name}."

print(user_name())

'''
Write a function called zeroed code that takes a list of
numbers as an argument. The code should zero (0) the first
and last number in the list. For example, if the input is [2, 5,
7, 8, 9], your code should return [0, 5, 7, 8, 0].
'''

def zeroed(num_lst):
    b = num_lst[1:-1]
    b.insert(0, 0)
    b.insert(b[-1], 0)
    return b

print(zeroed([2, 5,
7, 8, 9]))
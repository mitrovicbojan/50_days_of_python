'''
Writeafunction called hide_password that takes no parameters.
The function takes an input (a password) from a user and returns a
hidden password. For example, if the user enters "hello" as a
password, the function should return "****" as a password and tell
the user that the password is 4 characters long.

'''

def hide_password():
    user_input = input("Please enter your password: ")
    
    password_len = len(user_input)
    
    hidden =""
    for i in range(password_len):
        hidden = hidden + "*"
        
    return print(f"Your password {hidden} is {password_len} characters long.")
    
hide_password()

'''
Your new company has a list of figures saved in a database. The
issue is that these numbers have no separator. The numbers are
saved in a list in the following format:
[1000000, 2356989, 2354672, 9878098]. You have been
asked to write a code that will convert each of the
numbers in the list into a string. Your code should then add a
comma to each number as a thousand separator for
readability. When you run your code on the above list, your output
should be:
['1,000,000','2,356,989','2,354,672','9,878,098’]
Write a function called convert_numbers that will take
one argument, the list of numbers above.
'''

def convert_numbers(lst):
    converted_list =[]
    for i in lst:        
        converted_list.append(f"{i:,}")
    
    return print(converted_list)

convert_numbers([1000000, 2356989, 2354672, 9878098])
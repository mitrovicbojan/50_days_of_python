'''
Multiply Words
s = "love live and laugh"

Write a function called multiply_words that takes a string as an
argument and multiplies the length of each word in the string by the
length of other words in the string. For example, the string above
should return 240: love (4), live (4), and (3), laugh (5).
However, your function should only multiply words with all
lowercase letters. If a word has one uppercase letter, it should be
ignored. For example, the following string: s = "Hate war love
Peace" should return 12 - war (3) love (4). Hate and Peace will
be ignored because they have at least one uppercase letter.

'''
def multiply_words(text):
    
    lst = text.split()
    lower_list = []
        
    for i in lst:
        if i.islower():
            lower_list.append(i)
            
    first_len = len(lower_list[0])        
        
    for j in range(1, len(lower_list)):
        first_len *= len(lower_list[j])
            
    return print(first_len)

multiply_words("love live and laugh")

'''
Create a simple calculator. The calculator should be able to perform the
following basic math operations: add, subtract, divide, and
multiply. The calculator should take input from users. The calculator
should be able to handle ZeroDivisionError, NameError, and
ValueError.
'''

import operator

def calculator():
    try:
        first_num = int(input("Please enter number: "))
        user_calc = input("Please choose operator +, -, /, * : ")
        scnd_num = int(input("Please enter another number: "))
        
        if user_calc not in ["+", "-", "*", "/"] or len(user_calc) < 1:
            print("Please choose a valid operator (+,-,*,/).")
        
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("You cannot divide number by zero.")
    else:
        if user_calc == '+':
            return operator.add(first_num, scnd_num)
        if user_calc == '-':
            return operator.sub(first_num, scnd_num)
        if user_calc == '*':
            return operator.mul(first_num, scnd_num)
        if user_calc == '/':
            return operator.truediv(first_num, scnd_num)
    return 'Try again'

print(calculator())
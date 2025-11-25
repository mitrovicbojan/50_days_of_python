'''
Write a function called user_name, that creates a username for
the user. The function should ask a user to input their name. The
function should then reverse the name and attach a randomly
issued number between 0 and 9 at the end of the name. The
function should return the username.

'''
import random
def user_name():
    
    name_input = input("Please enter your name: ")
    
    reverse_name = name_input[::-1]
    
    rnd_num = random.randint(0,9)
    
    user_name = reverse_name + str(rnd_num)
    return f"your username is: {user_name}"

print(user_name())

'''
names = [ "Peter","Jon","Andrew"]

Write a function called sort_length that takes a list of strings as
an argument and sorts the strings in ascending order according to
their length. For example, the list above should return:
['Jon','Peter','Andrew']
Do not use the built-in sort functions.
'''
names = [ "Peter","Jon","Andrew"]
def sort_length(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if len(lst[i]) > len(lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst
print(sort_length(names))
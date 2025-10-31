'''
Write a function called only_floats, which has two parameters, a
and b, and returns 2 if both arguments are floats, 1 if only one
argument is a float, and 0 if neither argument is a float. If you
pass (12.1, 23) as an argument, your function should return 1.
'''

def only_floats(a,b):
    if type(a) == float and type(b) == float:
        return 2
    elif type(a) == float or type(b) == float:
        return 1
    else:
        return 0
    
    
result = only_floats(15,23.33)
print(result)

'''
Write a function called word_index that takes one argument, a
list of strings, and returns the index of the longest word in the list.
If there is no longest word (if all the strings are of the same length),
the function should return zero (0). For example, the first list below
should return 2.
Extra Challenge: Index of the Longest Word
words1 = ["Hate","remorse","vengeance"]
And this list below, should return zero (0)
words2 = ["Love","Hate"]
'''
words1 = ["Hate","remorse","vengeance"]
words2 = ["Love","Hate"]

def word_index(lst):
    return "hello"
    
    
lst_index = word_index(words1)
print(lst_index)
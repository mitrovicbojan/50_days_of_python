'''
Reverse a String

str1 = "the love is real"

Write a function called read_backwards that takes a string as
an argument and reverses it. The string above, for example, should
return: "real is love the."

'''

def read_backwards(text):
    
    lst = list(reversed(text.split()))
    rev_str = " ".join(lst)
    return print(rev_str)


read_backwards("the love is real")
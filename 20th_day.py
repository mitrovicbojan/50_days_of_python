'''
Write a function called capitalize. This function takes a string as
an argument and capitalizes the first letter of each word. For
example,
"i like learning" becomes "I Like Learning."

'''
def capitalize(string):
    
    my_lst = string.split(" ")
    upper_lst = []
    for i in my_lst:
        upper_lst.append(i.capitalize())
    upper_string = ' '.join(upper_lst)
    return upper_string

print(capitalize("i like learning."))

'''
str1 = 'leArning is hard, bUt if You appLy youRself ' \ 'you can achieVe success'

You are given a string of words. Some of the words in the string
contain uppercase letters. Write a code that will return all the
words that have an uppercase letter. Your code should return a
list of the words. Each word in the list should be reversed. Here
is how your output should look:
['gninrAel','tUb','uoY','yLppa','flesRuoy','eVeihca']
'''
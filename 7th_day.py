'''
Write afunction called string_range that takes a single number
and returns a string of its range. The string characters should be
separated by dots(.). For example, if you pass 6 as an argument,
your function should return "0.1.2.3.4.5.
"

'''

def string_range(num):
    my_str=""
    for i in range(0, num):
        my_str = my_str + str(i) + "."
    
    return print(my_str) 
    
string_range(6)

'''
You are given a list of names, and you are asked to write a code that
returns all the names that start with "S." Your code should return
a dictionary of all the names that start with S and how many times
they appear in the dictionary. Here is a list below:
names = ["Joseph", "Nathan", "Sasha", "Kelly","Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
Your code should return: {"Sasha": 1,"Sera": 2}

'''

names = ["Joseph", "Nathan", "Sasha", "Kelly","Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

s_names = []
for name in names:
    if name[0] == 'S':
        s_names.append(name)


s_names_dict = {name: s_names.count(name) for name in s_names}
print(s_names_dict)

# different way

name_dict = {name: names.count(name) for name in names if name[0]== "S"}

print(name_dict)
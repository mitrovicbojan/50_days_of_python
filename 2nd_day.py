'''
Day 2: Strings to Integers
Write a function called convert_add that takes a list of strings
as an argument, converts them to integers, and sums the list. For
example, ["1","3","5"] should be converted to [1, 3, 5] and
summed to 9.
'''

def convert_add(lst):
    int_list = []
    
    for i in lst:
        int_list.append(int(i))
        
    return sum(int_list)
   

result = convert_add(["1","3","5"])
print(result)

'''
Write a function called check_duplicates that takes a list of
strings as an argument. The function should check if the list has
any duplicates. If there are duplicates, the function should
return a list of duplicates. If there are no duplicates, the
function should return "no duplicates.
" For example, the list of
fruits below should return ["apple","banana"], and the list
of names should return "no duplicates."
fruits = ['apple', 'orange', 'banana', 'apple', 'banana'] names =
['Yoda', 'Moses', 'Joshua', 'Mark']

'''
fruits = ['apple', 'orange', 'banana', 'apple', 'banana']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

def check_duplicates(lst):
    
    unique = set()
    duplicates = set()
    
    for i in lst: 
        if i in unique:
            duplicates.add(i)
        else:
            unique.add(i)
    
    if not duplicates:
        return "No duplicates."
    else: 
        dbls = list(duplicates)
        return dbls
    
    
print(check_duplicates(names))



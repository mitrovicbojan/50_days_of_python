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
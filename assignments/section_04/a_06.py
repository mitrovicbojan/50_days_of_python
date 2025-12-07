# Assignment 6

"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.

So "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""

# Your Code Below:

def last2(string):
    if len(string) <=2:
        return 0
    last_two = string[len(string) - 2:]
    counter = 0
    
    for i in range(len(string) - 2):
        sub = string[i:i+2]
        
        if sub == last_two:
            counter = counter + 1
    return counter    

print(last2('axxxxaaxx'))

# print(last2('hixxhi')) #→ 1
# print(last2('xaxxaxaxx')) #→ 1
# print(last2('axxxxaaxx')) #→ 3

'''
Write a function called equal_strings. The function takes
two strings as arguments and compares them. If the strings
are equal (if they have the same characters and have equal
length), it should return True; if they are not, it should
return False. For example,
"love" and "evol" should return
True.

'''
def equal_strings(str1, str2):
    
    return sorted(str1) == sorted(str2)

print(equal_strings("love", "evol"))

'''
Write a function called swap_values. This function takes a
list of numbers and swaps the first element with the last
element. For example, if you pass [2, 4, 67, 7] as a
parameter, your function should return.
[7, 4, 67, 2].
'''
def swap_values(lst):
    last = lst.pop()
    first = lst.pop(0)
            
    return [last] + lst + [first]

print(swap_values([2, 4, 67, 7]))


# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# your code below:

def merge_lists(lst, lst2):
    
    new_list = lst + lst2
    
    return new_list

print(merge_lists([1,2,3,4], [5,6,7,8]))
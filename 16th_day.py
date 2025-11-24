'''
Write a function called sum_list with one parameter that takes a
nested list of integers as an argument and returns the sum of the
integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an
argument, your function should return a sum of 33.

'''

def sum_list(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
           total += sum_list(item)
        else:
            total += item
    
    return total
    

print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))


'''
nested_list = [[12, 34, 56, 67], [34, 68, 78]]
Write a code that generates a list of the following numbers from
the nested list above: 34, 67, 78. Your output should be another
list: [34, 67, 78]. The list output should not have duplicates.
'''
nested_list = [[12, 34, 56, 67], [34, 68, 78]]
def new_list(lst):
    target = [34,67,78]
    result = []
    seen = set()
    
    for i in target:
        for num in lst:
            if i in num and i not in seen:
                result.append(i)   
                seen.add(i)
                break
    
    return result
    
print(new_list(nested_list))
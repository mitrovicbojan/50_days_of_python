'''
Write a function called make_tuples that takes two equal lists
and combines them into a list of tuples. Your code should check
that the input lists are of the same length. For example, if list a is
[1, 2, 3, 4] and list b is [5, 6, 7, 8], your function should return
[(1, 5), (2, 6), (3, 7), (4, 8)]. If the lists are not of equal length,
your function should raise a ValueError.

'''

def make_tuples(list_a, list_b):
    
    if len(list_a) != len(list_b):
        return ValueError("Lists are not equal in length.")
    else:
        return list(zip(list_a, list_b))               
        

print(make_tuples([1, 2, 3, 4], [5, 6, 7, 8]))


'''
Write a function called even_or_average that asks a user to
input five numbers. Once the user is done, the code should
return the largest even number in the inputted numbers. If
there is no even number in the list, the code should return the
average of all the five numbers.
'''

def even_or_average():
    
    lst = []
    even_nums = []
    count = 0
    
    while count < 5:
        user_nums = input(f"Please 5 enter numbers ({count + 1}/5): ")
        
        try: 
            num = int(user_nums)
            
            if num % 2 == 0:
                even_nums.append(num)
                
            lst.append(num)
            count +=1
        except ValueError: 
            print("Please enter number.")
    
    if len(even_nums) != 0:
        return max(even_nums)
    else:
        avg = sum(lst) / 5
        return avg
    
                          
    
print(even_or_average())

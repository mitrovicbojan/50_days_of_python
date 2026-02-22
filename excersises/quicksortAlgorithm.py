'''
The quick_sort function should take a list of integers as input
and return a new list of these integers in sorted order from least to greatest.

To implement the algorithm, you should:

Choose a pivot value from the elements of the input list 
(use the first or the last element of the list).
Partition the input list into three sublists: 
one with elements less than the pivot, one with elements equal 
to the pivot, and one with elements greater than the pivot.
Recursively call quick_sort to sort the sublists and 
concatenate the sorted sublists to produce the final sorted list. 
'''

def quick_sort(array):    
    if len(array) == 0 or len(array) == 1:
        return array
        
    pivot_value = array[0]      
        
    smaller_value = []
    greater_value = []
    equal_value = []
    
   
       
    for i in array:
        if i < pivot_value:
            smaller_value.append(i)
        elif i > pivot_value:
            greater_value.append(i)
        elif i == pivot_value:
            equal_value.append(i)   
    sorted_smaller = quick_sort(smaller_value)
    sorted_greater = quick_sort(greater_value)    
    
    return sorted_smaller + equal_value + sorted_greater

print(quick_sort([20, 3, 14, 1, 5]))
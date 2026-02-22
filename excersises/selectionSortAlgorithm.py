'''
You should define a function named selection_sort.
Your selection_sort function should have one parameter that represents 
the list of items.
Your selection_sort function should take a list and sort the 
items in place from smallest to largest.
Your selection_sort function should modify the input 
list in-place, and return it once it's sorted.
Your selection_sort function should follow the selection 
sort algorithm, swapping the 
smallest element from the unsorted portion of the list with 
the first unsorted element.
Your selection_sort function should not perform unnecessary 
swaps when the smallest element is already in the correct position.
Your selection_sort function should not use either the built-in 
sort() method or sorted() function. 
'''

def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(min_index + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
        
    return array
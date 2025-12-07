# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""

# Your Code Below:

def grow_string(string):
    result = ''
    for i in range(len(string)):
        result = result + string[:i+1]
    
    return result

print(grow_string('Code'))
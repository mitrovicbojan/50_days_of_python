'''
Write a function called register_check that checks how many
students are in school. The function takes a dictionary as an
argument. If the student is in school, the dictionary says "yes." 
If the student is not in school, the dictionary says "no." Your function
should return the number of students in school. Using the dictionary
below, your function should return 3.

register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
'''
register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}

def register_check(dict):
    students_in = 0
    for i in dict.values():
        if i == 'yes':
            students_in = students_in + 1 
    
    return f"Number of students in school is: {students_in}."

print(register_check(register))

'''
names = ["kerry", "dickson", "John", "Mary","carol","Rose","adam"]

You are given a list of names above. This list is made up of names
win lowercase and uppercase letters. Your task is to write a code
that will return a tuple of all the names in the list that only have
lowercase letters. Your tuple should have names sorted
alphabetically in descending order. Using the list above, your code
should return:
('kerry','dickson','carol','adam')

'''
'''
Student Grades

Create a Student class:

Attributes: name and grades (list of floats, default empty list).

Methods:

add_grade(grade) → adds grade to list.

average() → returns the average grade (rounded to 2 decimals).

__str__() → "Student <name>, Average: <average>".

'''

class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []
        self._average = self._calculate_average()
                
    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            raise ValueError("Please enter valid numeric grades.")
        self.grades.append(grade)
        self._average = self._calculate_average()
    
    def _calculate_average(self):
        if not self.grade:
            return 0
        sum_grades = sum(self.grades)
        avg = round(sum_grades / len(self.grades), 2)
        return avg
    
    @property
    def average(self):
        return self._average
    
    def __str__(self):
        return f"Student: {self.name}\nAverage: {self.average}"
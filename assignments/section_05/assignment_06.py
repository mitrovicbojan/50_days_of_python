'''
Circle Operations
Problem Statement:
You are tasked with creating a Python class for mathematical operations related to circles. The class should encapsulate the functionality required for computing both the area and perimeter of a circle. Additionally, you will extend the functionality by adding a method to compute the sector area of a circle, given the radius and central angle in degrees.

Requirements:
The CircleOps class should have the following:

Static Data Member

PI: Denoting the value of PI (3.14).

Methods

getCircleArea(radius): This method should take the radius of a circle as a parameter and return the area of the circle.

getCirclePerimeter(radius): This method should take the radius of a circle as a parameter and return the perimeter (circumference) of the circle.

getSectorArea(radius, angle): This method should take the radius of the circle and the angle (in degrees) of the sector as parameters and return the area of the sector.

Instructions:

Implement the getCircleArea, getCirclePerimeter, and getSectorArea methods inside the CircleOps class.

The methods should correctly calculate the respective values using the provided radius and angle, as well as the value of PI (CircleOps.PI).

Circle Formulae:

Area of a Circle: area = PI * radius * radius

Perimeter of a Circle (Circumference): perimeter = 2 * PI * radius

Area of a Sector: sector_area = (angle / 360) * PI * radius * radius
'''
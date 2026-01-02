'''
Average Calories
Write a function called average_calories that calculates the
average calorie intake of a user. The function should ask the user to
input their calorie intake for any number of days, and once they hit
"done," it should calculate and return the average intake.
'''

def average_calories():
    calories = []
    while True:
        user_calorie = input("Enter a number of calories or done if you wish to quit: ")
        if user_calorie == 'done':
            break
        calories.append(int(user_calorie))
    
    result = round(sum(calories) / len(calories), 2)
    
    return print(f"Your average daily calorie intake is {result}")

average_calories()
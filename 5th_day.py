'''
Createafunction called my_discount. The function takes no
arguments but asks the user to input the price and the discount
(percentage) of the product. Once the user inputs the price and
discount, it calculates the price after the discount. The function
should return the price after the discount. For example, if the user
enters 150 as the price and 15% as the discount, your function
should return 127.5.

'''
def my_discount():
    while True:
        try:
            # Ask for inputs once
            price_input = input("Please enter price: ").strip()
            discount_input = input("Please enter discount: ").strip()

            # Convert price
            price = float(price_input)

            # Handle discount (with or without %)
            if "%" in discount_input:
                discount_input = discount_input.replace("%", "")
            
            discount = float(discount_input)

            # Convert percentage to decimal if needed
            if discount > 1:
                discount /= 100.0

            # Calculate final price
            final_price = price * (1 - discount)
            return final_price

        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")

price_after_discount = my_discount()
print(price_after_discount)

'''
You work for a school, and your boss wants to know how many
female and male students are enrolled in the school. The school has
saved the students on a list. Your task is to write a code that will
count how many males and females are in the list. Here is a list
below:
students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female','male','Female','Male','Female','Male','female']

Your code should return a list of tuples. The list above should
return: [("Male", 7), ("Female", 6)]

'''

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female','male','Female','Male','Female','Male','female']

def count_student_sex(lst):
    students_sex_list = [i.lower() for i in lst]
    return print(students_sex_list)

count_student_sex(students)
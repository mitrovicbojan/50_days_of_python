'''
Write a function called your_vat. The function has no
parameters. The function asks the user to input the price of an
item and VAT (VAT should be a percentage). The function should
return the price of the item plus VAT. If the price is 220 and the
VAT is 15%, your code should return a VAT-inclusive price of 253.
Check to see if your code can handle ValueError and negative
inputs from the user. Ensure the code runs until valid numbers are
entered. (Hint: Your code should include a while loop.)

'''

def your_vat():
    while True:
        try:
            price_input = int(input("Enter price: "))
            vat_input = int(input("Enter VAT: "))
            
            if price_input > 0 and vat_input > 0:
                total = price_input + (price_input * (vat_input) / 100)
                
                return total
            
        except ValueError:
            print("Please enter correct price and VAT.")
        

print(your_vat())

'''
Write a function called python_snakes that takes a number as
an argument and creates the pyramid shape using the number’s
range. (Hint: Use the loops and emoji libraries for snake emojis.)
'''
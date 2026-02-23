''' 
Implement the Luhn Algorithm

ou should define a function named verify_card_number 
that takes a string of digits (representing a card number) 
and verifies whether it is valid according to the 
Luhn algorithm.

Within the verify_card_number function:

You should handle any dashes or spaces that may be 
present in the card number passed to it.
Return VALID! if the card number is valid; 
otherwise, return INVALID!.
When you complete the project, you should see 
the following messages depending on the input:

Card Number	Message
453914889	VALID!
4111-1111-1111-1111	VALID!
1234 5678 9012 3456	INVALID!
'''

def verify_card_number(string):
    #remove white space and dash
    string_num = string.replace(" ", "").replace("-","") 
    
    #create list of numbers   
    array_num = [int(num) for num in string_num]
    
    array_num.reverse()
    
    x = slice(1, len(array_num), 2)
    y = slice(0, len(array_num), 2)
    
    dbl_val_arr = [num * 2 for num in array_num[x]]
    sng_val_arr = array_num[y]
    
    val_arr = []
    for i in dbl_val_arr:
        if i > 9:
            first_digit = int(i / 10)
            second_digit = i % 10
            val_arr.append(first_digit)
            val_arr.append(second_digit)
        else:            
            val_arr.append(i)
    
    sum_arr = sum(val_arr + sng_val_arr)
    
    if sum_arr % 10 == 0:
        return 'VALID!'
    else:
        return "INVALID!"
    
verify_card_number('1234 5678 9012 3456')
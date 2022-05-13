# NAME OF AUTHOR: Matteo 
# NAME OF THE PROGRAM:  
print("How to calculate the total cost of items including tax")
# DATE OF CREATION:   05-12-2022
# PURPOSE OF PROGRAM:  
print("Calculating the cost of items with tax")

# VARIABLE DEFINITION


price_of_combined_items = 0
price_of_combined_with_tax = 0
tax = 0



# PROCESSING
for i in range(10): 
    item = int(input())
    tax += item * 0.13
    price_of_combined_items += item
price_of_combined_with_tax = tax + price_of_combined_items 


# OUTPUT
print("your final payment is " + str(price_of_combined_with_tax))
print("your final payment is " + str(price_of_combined_items))
print("your tax is " + str(tax))


#Tip calculator

print('Welcome to Asanka Hotel')

# user enters the food charges
food_charges = float(input('Enter your charges '))                                

# calculate tip percentage
tip_percentage = 0.18                                                         

# calculate sales tax
sales_tax = 0.07                                                                

# calculate tip amount
tip_amount = float(food_charges * tip_percentage)                                 

# calculate tax amount
tax_amount = float(food_charges * sales_tax)                                    

# calculate grand total
grand_total = float(food_charges + tip_amount + tax_amount)                  

# print out tip amount, tax amount and grand total
print(f' tip = ${tip_amount:.2f}\n sales_tax = $ {tax_amount:.2f}\n grand_total = $ {grand_total:.2f}')

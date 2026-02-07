# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

#prices
HotDogPrice = 3.50
ChiliDogPrice = 4.50
CheesePrice = 0.50
PeppersPrice = 0.75
OnionsPrice = 1.00
TaxRate = 0.07
subtotal= 0.0

#hot dog types
Hotdog_type = input("Enter the type of hot dog (Hot Dog or Chili Dog): ")

if Hotdog_type == "Hot Dog":
     subtotal = HotDogPrice
elif Hotdog_type == "Chili Dog":
    subtotal = ChiliDogPrice

else:
    print("Invalid hot dog type. Please enter 'Hot Dog' or 'Chili Dog'.")
    exit()

#toppings for hotdog
cheese = input("Do you want cheese? (yes or no): ")
if cheese == "yes":
    subtotal += CheesePrice
peppers = input("Do you want peppers? (yes or no): ")
if peppers == "yes":
    subtotal += PeppersPrice
onions = input("Do you want grilled onions? (yes or no): ")
if onions == "yes":
    subtotal += OnionsPrice

tax= subtotal * TaxRate
total = subtotal + tax

print("Hot Dog Cost: $", format(subtotal, '.2f'))
print("Tax: $", format(tax, '.2f'))
print("Total Cost: $", format(total, '.2f'))
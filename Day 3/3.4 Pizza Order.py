# 🚨 Don't change the code below 👇
from cgitb import small
from statistics import median


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_medium_large = 3
cheese = 1

if size == "S":
    bill = small_pizza
elif size == "M":
    bill = medium_pizza
elif size == "L":
    bill = large_pizza

if add_pepperoni == "Y":
    if size == "S":
        bill += pepperoni_small
    else:
        bill += pepperoni_medium_large
        
if extra_cheese == "Y":
    bill += cheese
    
print(f"Your final bill is: ${bill}.")
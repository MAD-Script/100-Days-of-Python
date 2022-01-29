# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)
years_till_90 = 90 - age_int

day = years_till_90 * 365
week = years_till_90 * 52
month = years_till_90 * 12

print(f"You have {day} days, {week} weeks, and {month} months left.")
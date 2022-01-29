# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / height ** 2 

if bmi < 18.5:
    bmi_string = "are underweight"
elif bmi < 25:
    bmi_string = "have a normal weight"
elif bmi < 30:
    bmi_string = "are slightly overweight"
elif bmi < 35:
    bmi_string = "are obese"
else:
    bmi_string = "are clinically obese"

bmi_rounded = round(bmi)
print(f"Your BMI is {bmi_rounded}, you {bmi_string}.")
print("welcome to the tip calculator")
bill = float(input("What was the total bill?\n$ "))
people = float(input("How many people to split the bill? \n->"))
tip_percent = float(
    input("What percentage tip would you like to give? 10, 12, or 15?\n% "))

total_bill = bill * tip_percent/100 + bill
bill_per_person = "{:.2f}".format(total_bill/people)

print("Each person should pay: $"+bill_per_person)

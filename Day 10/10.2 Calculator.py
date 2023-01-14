

def add(num1, num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    
}

num1 = int(input("Enter the First Num: "))

for operation in operations:
    print(operation)
    
operator = input("Pick one of the operators: ")

num2 = int(input("Enter the Second Num: "))


answer = operations[operator](num1,num2)


print(f"{num1} {operator} {num2} = {answer}")
    
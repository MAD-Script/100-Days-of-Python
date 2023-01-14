
# This code has intentional Bugs

from Calculator_art import logo

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

def calculator():
    
    print(logo)
    
    should_continue = True

    num1 = int(input("Enter the First Num: "))

    for operation in operations:
        print(operation)


    while(should_continue):
        
        operator = input("Pick one of the operators: ")

        num2 = int(input("Enter the Next Num: "))
        
        answer = operations[operator](num1,num2)
        
        print(f"{num1} {operator} {num2} = {answer}")
        
        num1 = answer
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y"
        
    if (not should_continue): calculator()
        

calculator()
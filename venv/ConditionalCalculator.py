def add():
    a = float(input("Please enter a number: "))
    b = float(input("Please enter another number: "))
    print(a+b)

def subtract():
    a = float(input("Please enter a number: "))
    b = float(input("Please enter another number: "))
    print(a-b)

def multiply():
    a = float(input("Please enter a number: "))
    b = float(input("Please enter another number: "))
    print(a*b)

def divide():
    a = float(input("Please enter a number: "))
    b = float(input("Please enter another number: "))
    print(a/b)

on = True
while on:
    operation = input("Please type +, -, *, / or q: ")
    if operation == '+':
        add()
    elif operation == '-':
        subtract()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'q':
        on = False
    else:
        print("no operation was chosen")
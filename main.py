a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

def Operation(a,b):
    Op=input("Enter the operation you want to perform (+, -, *, /): ")
    match Op:
        case "+":
            print(f"The sum of {a} and {b} is: {a+b}")
        case "-":
            print(f"The difference of {a} and {b} is: {a-b}")
        case "*":
            print(f"The product of {a} and {b} is: {a*b}")
        case "/":
            if b != 0:
                print(f"The quotient of {a} and {b} is: {a/b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation. Please enter one of the following: +, -, *, /.")
    Repeat=input("Do you want to perform another operation? (yes/no): ")
    if Repeat.lower() == "yes":
        Arg1=input("Do you want to use the same numbers? (yes/no): ")
        if Arg1.lower() == "yes":
            Operation(a,b)
        else:
            a=int(input("Enter the first number: "))
            b=int(input("Enter the second number: "))       
        Operation(a,b)
    else:
        print("Thank you for using the calculator. Goodbye!")

Operation(a,b)


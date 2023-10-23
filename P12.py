def calculator():
    num1 = complex(input("Enter the first number as 1+4j: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = complex(input("Enter the second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:    
            result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return

    print(f"Result: {num1} {operator} {num2} = {result}")

# Call the calculator function directly
calculator()

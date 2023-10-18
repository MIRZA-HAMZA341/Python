def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue

            print(f"Result: {num1} {operator} {num2} = {result}")
            
            another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if another_calculation.lower() != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    calculator()

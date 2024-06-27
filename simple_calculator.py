def calculator():
    # Function to perform the calculation
    def perform_operation(num1, num2, operation):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error! Division by zero."
        else:
            return "Invalid operation."

    # Get user input for numbers and operation
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ")

        # Perform the operation
        result = perform_operation(num1, num2, operation)

        # Display the result
        print(f"The result of {num1} {operation} {num2} is: {result}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values for numbers.")

# Run the calculator function
calculator()

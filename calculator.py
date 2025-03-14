print("Basic Calculator Program")

# User inputs
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Valid Operations
if operation not in ['+', '-', '*', '/']:
    print("Invalid operation. Please use +, -, *, /")
    exit()

    # perform the calculation
    result = None
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        if number2 == 0:
            print("Cannot divide by zero")
            exit()
        result = number1 / number2

        # Functions to format numbers as integers or floats
        def format_number(number):
            if number.is_integer():
                return int(number)
            else:
                return number
            
        # Output
        print(f"{format_number(number1)} {operation} {format_number(number2)} = {format_number(result)}")


        print("Thank you for using the calculator")
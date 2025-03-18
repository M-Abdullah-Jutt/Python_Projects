
# Greetings Message
print('Welcome! To Your Calculator')

# Addition Function
def add(x, y):
    return x + y

# Subtraction Function
def subtract(x, y):
    return x - y

# Multiplication Function
def multiply(x, y):
    return x * y

# Division Function
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Modulus Function
def modulus(x, y):
    return x % y

# Basic Operators of a Calculator
operators = ['addition', 'subtraction', 'multiply', 'division', 'modulus']

# Calculation Function
def calculation():
    # Ask user to type numbers first.
    first_number = float(input('Enter First Number: '))
    second_number = float(input('Enter Second Number: '))

    # Ask user to perform operation.
    operation = input('Write The Operation You Want To Perform: ').lower()

    # Conditional statements are used for building logic.
    if operation in operators:
        if operation == 'addition':
            result = add(first_number, second_number)
            print(f"Result: {round(result)}")
        elif operation == 'subtraction':
            result = subtract(first_number, second_number)
            print(f"Result: {round(result)}")
        elif operation == 'multiply':
            result = multiply(first_number, second_number)
            print(f"Result: {round(result)}")
        elif operation == 'division':
            result = divide(first_number, second_number)
            print(f'Result: {result}')
        elif operation == 'modulus':
            result = modulus(first_number, second_number)
            print(f"Result: {result}")
    else:
        # Display a user-friendly error message
        print(f"Please perform an operation from the following list: {', '.join(operators)}")

# Main Execution
if __name__ == "__main__":
    calculation()
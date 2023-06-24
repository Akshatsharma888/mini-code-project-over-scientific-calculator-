import math

# Function to perform basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Function to perform scientific operations
def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def logarithm(x, base):
    return math.log(x, base)

# Main calculator loop
def scientific_calculator():
    print("Scientific Calculator")
    print("Enter 'q' to quit")

    while True:
        print("\n[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Division")
        print("[5] Square Root")
        print("[6] Power")
        print("[7] Logarithm")

        choice = input("Enter your choice (1-7): ")

        if choice == 'q':
            break

        if choice in ['1', '2', '3', '4']:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))

            if choice == '1':
                result = add(x, y)
                operation = "+"
            elif choice == '2':
                result = subtract(x, y)
                operation = "-"
            elif choice == '3':
                result = multiply(x, y)
                operation = "*"
            elif choice == '4':
                result = divide(x, y)
                operation = "/"

            print(f"{x} {operation} {y} = {result}")

        elif choice == '5':
            x = float(input("Enter the number: "))
            result = square_root(x)
            print(f"Square root of {x} = {result}")

        elif choice == '6':
            x = float(input("Enter the base number: "))
            y = float(input("Enter the exponent: "))
            result = power(x, y)
            print(f"{x} raised to the power of {y} = {result}")

        elif choice == '7':
            x = float(input("Enter the number: "))
            base = float(input("Enter the logarithm base: "))
            result = logarithm(x, base)
            print(f"Logarithm of {x} with base {base} = {result}")

        else:
            print("Invalid choice. Please try again.")

# Start the scientific calculator
scientific_calculator()

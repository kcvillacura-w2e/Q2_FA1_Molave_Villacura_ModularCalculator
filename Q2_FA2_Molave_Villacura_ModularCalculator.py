# Function for addition
def add_numbers(num1, num2):
    return num1 + num2
# Function for subtraction
def subtract_numbers(num1, num2):
    return num1 - num2
# Function for multiplication
def multiply_numbers(num1, num2):
    return num1 * num2
# Function for division
def divide_numbers(num1, num2):
    if num2 <= 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2
# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Ask the user to choose an operation
print("Choose an operation:")
print("1 - Addition (+)")
print("2 - Subtraction (-)")
print("3 - Multiplication (*)")
print("4 - Division (/)")
choice = input("Enter your choice (1-4): ")
# Perform the selected operation
if choice == "1":
    result = add_numbers(num1, num2)
elif choice == "2":
    result = subtract_numbers(num1, num2)
elif choice == "3":
    result = multiply_numbers(num1, num2)
elif choice == "4":
    result = divide_numbers(num1, num2)
else:
    result = "Invalid choice!"
# Display the final answer
print("Result:", result)

# Assignment #4: Simple Calculator
# Task:
# Create a simple calculator that performs addition, subtraction, multiplication, or division based on user input.

# Requirements:

# Ask the user to enter two numbers.
# Ask the user to choose an operation: +, -, *, or /.
# Perform the operation and print the result.
# If the user enters an invalid operator, print an error message.

input_first = float(input("Enter First Number:"))
input_second = float(input("Enter Second Number:"))

input_operation = str(input("Select Operations \n Add = +\n Sub = -\n mul = *\n div = / \n choose : "))

if input_operation == "+" :
    print(f"Addition of {input_first} and {input_second} is: ", input_first + input_second)
elif input_operation == "-" :
    print(f"Substraction of {input_first} and {input_second} is: ", input_first - input_second)
elif input_operation == "*" :
    print(f"Multiplication of {input_first} and {input_second} is: ", input_first * input_second)
elif input_operation == "/" :
    print(f"Division {input_first} and {input_second} is: ", input_first / input_second)
else:
    print("You may gave Wrong Input, its ERROR, TRY AGAIN!")


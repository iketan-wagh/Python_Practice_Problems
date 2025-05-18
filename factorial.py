# Assignment #7: Factorial Calculator
# Task:
# Write a program to calculate the factorial of a number.

# Example:

# Input: 5
# Output: 120 (because 5×4×3×2×1 = 120)

# Requirements:

# Take a non-negative integer input.
# Use a for loop to calculate factorial.
# Print the result.

input_number = int(input("Enter a non-negative integer: "))

# Check if the number is negative
if input_number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, input_number + 1):
        factorial *= i  # Multiply factorial by each number from 1 to input_number
    print(f"Factorial of {input_number} is: {factorial}")

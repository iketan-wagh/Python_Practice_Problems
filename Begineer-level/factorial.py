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

input_user = int(input("Enter no to find Factorial:"))

factorial = 1

if input_user == 0:
    print("Factorial of Zero is 1")
else:
    for i in range(1, input_user+1) :
        factorial*=i
    print(factorial)
# Assignment #3: Positive, Negative, or Zero Checker
# Task:
# Write a Python program to check whether a number is positive, negative, or zero.

# Requirements:

# Take a number (integer or float) as input.
# Use if-elif-else to:
# Print "Positive number" if it's more than 0.
# Print "Negative number" if it's less than 0.
# Print "Zero" if it’s exactly 


input_user = float(input("Enter a Number: "))
if input_user>0:
    print("Positive number")
elif input_user<0:
    print("Negative number")
else:
    print("Zero")
    

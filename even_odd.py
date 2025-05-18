# Assignment #1: Even or Odd Checker
# Task:
# Write a Python program that takes a number as input and checks if it is even or odd.
# Requirements:
# Take an integer input from the user.
# Use an if-else statement to check if the number is even or odd.
# Print the appropriate message.

input_user= int(input("Enter No here:"))
if input_user % 2 == 0:
    print(f"{input_user} is a Even number")
else:
    print(f"{input_user} is a Odd number")
# Assignment #2: Number Range Checker
# Task:
# Write a Python program that checks if a given number is within a range of 10 to 50 (inclusive).

# Requirements:

# Take an integer input from the user.
# Use an if-else or if-elif-else to check:
# If the number is between 10 and 50 (inclusive), print: "Number is in range!"
# Otherwise, print: "Number is out of range."

input_user= int(input("Enter an Integer: "))
if input_user >= 10 and input_user <= 50:
    print("Number is in range!")
else:
    print("Number is out of range.")

# Alternative way

# if 10 <= input_user <= 50:
#     print("Number is in range!")
# else:
#     print("Number is out of range.")
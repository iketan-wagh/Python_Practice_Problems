# Assignment: Find All Unique Digits in a Number
# Task:
# Write a program that takes an integer input from the user and prints only the unique digits (i.e., digits that appear only once in the number).
# Requirements:
# Use a for loop

# Use a dictionary (or any method you prefer)

# Avoid using collections.Counter for now (you’ll do it manually)

# Handle input as string so you can loop over digits

input_num = input("enter no: ")
list_num = {}

for i in input_num:
    if i.isdigit():
        if i in list_num:
            list_num[i]+=1
        else:
            list_num[i]=1

for key, value in list_num.items():
    if value==1:
        print(f"unique values are: {key}")

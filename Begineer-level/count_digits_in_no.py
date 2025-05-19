# Challenge: Count the Frequency of Each Digit
# 📌 Task:
# Write a program that:

# Takes an integer input from the user

# Counts how many times each digit (0–9) appears in that number

# Prints the result in a readable format

input_num = input("enter no: ")
list_num = {}
for i in input_num:
    if i.isdigit():
        if i in list_num:
            list_num[i]+=1
        else:
            list_num[i]=1

# print(list_num)
    
for i in sorted(list_num):
    print(f"Digit {i}: {list_num[i]} times")
# Assignment #8: Count Even and Odd Digits
# Task:
# Write a Python program that takes a positive integer as input and counts how many even and odd digits are in the number.

# ✅ Example:
# Input: 123456

# Output:
# Even digits: 3  
# Odd digits: 3

# 💡 Hints:
# You can loop through each digit using a for loop.
# Use int(digit) % 2 == 0 to check if it’s even.
# Use counters: even_count += 1 and odd_count += 1


input_user = input("Enter Number: ")
even_count = 0
odd_count = 0
for i in input_user:
    if int(i)%2 == 0:
        even_count+=1
    else:
        odd_count+=1
print(f"Total Even no in above integer is: {even_count},\nTotal Odd no in above integer is: {odd_count} ")

    
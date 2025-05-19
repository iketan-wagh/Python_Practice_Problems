# Assignment #6: Sum of Digits
# Task:
# Write a program to calculate the sum of digits of a given number.

# Example:
# Input: 1234
# Output: 10 (because 1+2+3+4 = 10)

# Requirements:

# Take a positive integer as input.
# Extract each digit and add them.
# Print the final sum.

# 📌 Hint: Use loops or convert number to string.

i_int = input("input Numers to Add them: ")
store_num = 0
for i in i_int:
    store_num += int(i)

print(store_num)

    
    


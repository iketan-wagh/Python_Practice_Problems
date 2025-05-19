# 🎯 Next Assignment (#10): Find the Largest Digit
# Task:
# Write a program that takes a number as input and prints the largest digit in that number.

# Example:
# Input: 372549
# Output: 9

input_user = input("Enter a Number to find largest digit: ")
large_digit = 0
for i in input_user:
    int_i = int(i)
    if int_i > large_digit:
        large_digit = int_i

print(large_digit)
   
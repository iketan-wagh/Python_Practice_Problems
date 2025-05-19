# 🧮 Assignment #12: Fibonacci Series Generator
# 📌 Task:
# Write a Python program that takes an integer n from the user and prints the first n terms of the Fibonacci sequence.

# 🧾 Example:
# Input:

# Enter number of terms: 7
# Output:
# 0 1 1 2 3 5 8

# 💡 What is Fibonacci?
# The sequence starts with: 0, 1
# Each next number is the sum of the previous two.
# 🛠 Hints:
# Use a for loop.
# Start with two variables: a = 0, b = 1
# Loop n times and update:

input_user = int(input("Enter  number: "))
a = 0
b = 1
c = 0
for i in range(input_user+1):
    print(f"{i}, {a}")
    a, b = b, a + b,

    


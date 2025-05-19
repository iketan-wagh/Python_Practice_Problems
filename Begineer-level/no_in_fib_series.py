# 🧩 Challenge: Check if a Number is in the Fibonacci Sequence
# 📌 Task:
# Write a program that:
# Takes an integer input from the user.
# Checks if that number exists in the Fibonacci sequence.

# Prints "Yes, it is a Fibonacci number" if found, otherwise "No, it is not".

# ✅ Example:
# Input:

# Enter a number: 13
# Output:

# Yes, it is a Fibonacci number.

# 💡 Hint:
# Use a while loop or for loop to generate Fibonacci numbers until you reach or exceed the number.

# Then check:
# If the number is equal to any Fibonacci number → ✅ Yes
# If it goes past the number without a match → ❌ No

while True:
    input_user = int(input("Enter  number: "))
    a = 0
    b = 1

    while a < input_user:
        a, b = b, a + b
    
    if a == input_user:
        print("Yes, it is a Fibonacci number.")
    else:
        print("No, it is not a Fibonacci number.")










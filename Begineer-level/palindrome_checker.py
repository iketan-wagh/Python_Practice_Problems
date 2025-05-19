# Assignment #5: Palindrome Checker
# Task:
# Check if a word entered by the user is a palindrome (reads the same forwards and backwards).

# Example:
# Input: "madam" → Output: "It's a palindrome!"
# Input: "python" → Output: "Not a palindrome."

# Requirements:

# Take a string input.
# Ignore case (treat "Madam" and "madam" as equal).
# Reverse the string and compare.

input_word = input("Enter words: ")
nomr_str = input_word.lowers()
rev_str = nomr_str[::-1]
if nomr_str == rev_str:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")  
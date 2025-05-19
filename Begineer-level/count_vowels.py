#  Next Assignment (#11): Count Vowels in a Word
# Task:
# Write a Python program to count how many vowels (a, e, i, o, u) are in a word or sentence.

# 💡 Example:
# Input: "Hello World"
# Output: 3 vowels
input_user = input("Enter Words to find Vowel count: ")
vowel_list= []
processed_str = input_user.lower().strip()
for i in processed_str:
    
    if i in "aeiou":
        vowel_list += i
print(f"{len(vowel_list)} vowels")
    

# alternate & simple

# vowel_count = 0
# for i in processed_str:
#     if i in "aeiou":
#         vowel_count += 1
# print(f"{vowel_count} vowels")

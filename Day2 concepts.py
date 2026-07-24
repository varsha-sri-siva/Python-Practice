# ==================================
# Day 2 - Python Practice
# Comments
# Type Casting
# String Methods
# String Slicing
# ==================================

# Single Line Comment
print("Python Day 2")

"""
This is
a multi-line comment
"""

print("\n----------------")

# Type Casting

age = "20"

print(type(age))

age = int(age)

print(type(age))

print("\n----------------")

# String Methods

name = "varsha"

print(name.upper())
print(name.lower())
print(name.title())

sentence = "I like Java"

print(sentence.replace("Java", "Python"))

print(len(sentence))

text = "   Cyber Security   "

print(text.strip())

print("\n----------------")

# String Slicing

word = "PythonProgramming"

print(word[0])
print(word[-1])
print(word[0:6])
print(word[6:])
print(word[:10])

print("\n----------------")

# User Input

user = input("Enter your name: ")

print(user.upper())
print(user.lower())
print(user.title())

print("\n----------------")

print("Day 2 Practice Completed Successfully!")

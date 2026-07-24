# Day 2 - Python Comments, Type Casting, Strings

## 1. Comments

### What are Comments?

Comments are used to explain the code. Python ignores comments while executing the program.

### Types of Comments

### Single-line Comment

```python
# This is a single-line comment
print("Hello")
```

### Multi-line Comment

```python
"""
This is a
multi-line comment.
"""
```

### Why do we use Comments?

- Explain the code.
- Improve readability.
- Make debugging easier.
- Help other developers understand the code.

---

# 2. Type Casting

## What is Type Casting?

Type casting means converting one data type into another.

### Common Type Casting Functions

- int()
- float()
- str()
- bool()

### Example

```python
age = "20"

print(type(age))

age = int(age)

print(type(age))
```

Output

```
<class 'str'>
<class 'int'>
```

---

# 3. Strings

## What is a String?

A string is a sequence of characters enclosed in single or double quotes.

Example

```python
name = "Varsha"
```

---

# 4. String Methods

Python provides many built-in methods to manipulate strings.

### upper()

Converts text into uppercase.

```python
name = "varsha"
print(name.upper())
```

Output

```
VARSHA
```

---

### lower()

Converts text into lowercase.

```python
print("HELLO".lower())
```

Output

```
hello
```

---

### title()

Capitalizes the first letter of every word.

```python
print("python programming".title())
```

Output

```
Python Programming
```

---

### replace()

Replaces one word with another.

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output

```
I like Python
```

---

### len()

Returns the length of a string.

```python
print(len("Cyber Security"))
```

Output

```
15
```

---

### strip()

Removes extra spaces.

```python
text = "  Hello  "

print(text.strip())
```

---

# 5. String Slicing

## What is String Slicing?

String slicing extracts a part of a string.

Syntax

```python
string[start:end]
```

Example

```python
text = "CyberSecurity"

print(text[0:5])
```

Output

```
Cyber
```

### More Examples

```python
text = "Python"

print(text[0])
print(text[-1])
print(text[0:3])
print(text[2:])
print(text[:4])
```

---

# What I Learned Today

- Comments
- Type Casting
- Strings
- String Methods
- String Slicing

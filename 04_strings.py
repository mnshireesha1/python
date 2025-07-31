name = "Shireesha"
quote = 'Python is fun!'
multiline = """This
is a
multiline string"""
print(name)
print(quote)
print(multiline)

# Accessing characters
text = "Python"
print(text[0])      # P
print(text[-1])     # n
print(text[1:4])    # yth
print(text[:3])     # Pyt
print(text[3:])     # hon

# String Length
n =len("Shree")  # 5
print(n)

# Strings are Immutable
text = "Python"
#text[0] = 'J'  ❌ Error: strings are immutable

# Strings methods
s = "Python"
s.upper()        # 'PYTHON'
s.lower()        # 'python'
s.capitalize()   # 'Python'
s.title()        # 'Python'
print(s)

# Trimming
print("  Hello  ".strip())     # 'Hello'
print("***Welcome***".strip("*"))  # 'Welcome'

# Searching & Counting
s = "banana"
print(s.count("a"))         # 3
print(s.find("na"))        # 2
print(s.rfind("na"))        # 4
print("apple" in s )        # False

# Replace
str1 = "hello world".replace("world", "Python")  # 'hello Python'
print(str1)

# String Operations
print("a" + "b")     # 'ab' (concatenation)
print("hi" * 3)      # 'hihihi' (repetition)

# String Splitting & Joining
text = "apple,banana,grape"
parts = text.split(",")       # ['apple', 'banana', 'grape']
print(parts)
print("-".join(parts))               # 'apple-banana-grape'

# Check string content
s = "Python3"
s.isalpha()     # False
s.isdigit()     # False
s.isalnum()     # True
"123".isdigit() # True
"abc".isalpha() # True

# Looping through Strings
for char in "Shree":
    print(char)

# Reverse a String
s = "hello"
print(s[::-1])        # 'olleh'

# Escape Characters
print("He said \"Hello\"")   # He said "Hello"
print('It\'s OK')            # It's OK
print("Line1\nLine2")        # newline
print("Tab\tSpace")          # tab space

#Raw Strings
path = r"C:\Users\Shree\Docs"
print(path)                  # C:\Users\Shree\Docs

# Built-in Functions
print(max("apple"))        # 'p'
print(min("apple"))        # 'a'
print(sorted("banana"))    # ['a', 'a', 'a', 'b', 'n', 'n']
print(list("Hi"))          # ['H', 'i']

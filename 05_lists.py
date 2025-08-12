fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]

print(fruits)
print(mixed)
print(nested)

empty_list = []
numbers = list(range(1, 6))   # [1, 2, 3, 4, 5]
chars = list("python")        # ['p', 'y', 't', 'h', 'o', 'n']

print(empty_list)
print(numbers)
print(chars)

# indexing & slicing
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])     # apple
print(fruits[-1])    # date
print(fruits[1:3])   # ['banana', 'cherry']
print(fruits[::-1])  # Reverse list

# changing list items
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']

# adding items
fruits.append("elderberry")    # Add at end
fruits.insert(1, "banana")     # Insert at index 1
fruits.extend(["fig", "grape"]) # Add multiple
print(fruits)

# removing items
fruits.remove("banana")   # Remove by value
popped_item = fruits.pop(2) # Remove by index
del fruits[0]              # Delete first element
fruits.clear()             # Empty list

# list operations
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # Concatenate
print(a * 2)  # Repeat list

# searching & counting
nums = [1, 2, 3, 2, 4, 2]
print(nums.index(3))   # 2
print(nums.count(2))   # 3

# sorting & reversing
nums = [5, 2, 9, 1]
nums.sort()            # Ascending
nums.sort(reverse=True) # Descending
print(sorted(nums))    # Returns new sorted list
nums.reverse()         # Reverse order

# list comprehesions
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# copying lists
a = [1, 2, 3]
b = a              # Same reference (changes affect both)
c = a.copy()       # Independent copy
d = list(a)        # Another copy method
print(a)
d.remove(3)
print(a)
print(d)

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[0][1])  # 2

# useful built-in functions
nums = [10, 20, 30, 40]
print(len(nums))  # 4
print(max(nums))  # 40
print(min(nums))  # 10
print(sum(nums))  # 100

fruits = ("apple", "banana", "cherry")
mixed = (1, "hello", 3.14, True)

# creating tuples
empty_tuple = ()
one_item_tuple = ("apple",)  # comma is important!
without_parentheses = 1, 2, 3  # tuple packing
tuple_from_list = tuple([1, 2, 3])
print(without_parentheses)

# accessing elements
fruits = ("apple", "banana", "cherry")
print(fruits[0])    # apple
print(fruits[-1])   # cherry
print(fruits[1:3])  # ('banana', 'cherry')

# tuple immutability
fruits = ("apple", "banana", "cherry")
# fruits[1] = "blueberry" ❌  ERROR: Tuples cannot be changed

#tuple operations
a = (1, 2, 3)
b = (4, 5)
print(a + b)  # (1, 2, 3, 4, 5)
print(a * 2)  # (1, 2, 3, 1, 2, 3)

# searching & counting
nums = (1, 2, 3, 2, 4, 2)
print(nums.index(3))  # 2
print(nums.count(2))  # 3

# tuple unpacking
person = ("Ravi", 25, "Engineer")
name, age, job = person
print(name)  # Ravi

# you can also use * to unpack
numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers
print(rest)  # [3, 4, 5]

# nested tuples
nested = ((1, 2), (3, 4))
print(nested[1][0])  # 3

# converting tuples
fruits = ("apple", "banana", "cherry")
fruits_list = list(fruits)
fruits_list.append("date")
fruits = tuple(fruits_list)

# built in functions with tuples
nums = (10, 20, 30)
print(len(nums))   # 3
print(max(nums))   # 30
print(min(nums))   # 10
print(sum(nums))   # 60

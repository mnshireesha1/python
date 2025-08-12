fruits = {"apple", "banana", "cherry"}

# creating sets
empty_set = set()  # Correct way
set_with_data = {"apple", "banana", "cherry"}
set_from_list = set([1, 2, 3, 3])  # {1, 2, 3} duplicates removed

# adding & removing elements
fruits = {"apple", "banana"}
fruits.add("cherry")      # Add single element
fruits.update(["mango", "grape"])  # Add multiple elements
print(fruits)

fruits.remove("banana")   # Remove specific item (error if not found)
fruits.discard("banana")  # Remove without error
fruits.pop()              # Remove random element
fruits.clear()            # Empty set
print(fruits)

# set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union → {1, 2, 3, 4, 5, 6}
print(A & B)   # Intersection → {3, 4}
print(A - B)   # Difference → {1, 2}
print(A ^ B)   # Symmetric Difference → {1, 2, 5, 6}

# membership & looping
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)  # True

for fruit in fruits:
    print(fruit)

# frozen sets (immutable sets)
frozen = frozenset([1, 2, 3])
# frozen.add(4) ❌ Error (immutable)
print(frozen)

# useful methods
A = {1, 2, 3}
B = {2, 3}

print(A.issubset(B))      # False
print(A.issuperset(B))    # True
print(A.isdisjoint(B))    # False

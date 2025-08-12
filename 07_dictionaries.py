student = {
    "id": 101,
    "name": "Ravi",
    "marks": 85
}

# creating dictionaries
empty_dict = {}
dict_with_data = {"name": "Ravi", "age": 25}
dict_from_pairs = dict([("name", "Ravi"), ("age", 25)])
dict_from_kwargs = dict(name="Ravi", age=25)
print(dict_with_data)
print(dict_from_pairs)
print(dict_from_kwargs)

# accessing data
student = {"name": "Ravi", "age": 25}
print(student["name"])  # Ravi
print(student.get("age"))  # 25
print(student.get("grade", "Not Assigned"))  # Default value

# Adding & Updating data
student = {"name": "Ravi", "age": 25}
student["grade"] = "A"  # Add new key
student["age"] = 26     # Update value

# removing data
student = {"name": "Ravi", "age": 25, "grade": "A"}
student.pop("age")         # Removes "age"
student.popitem()          # Removes last inserted item
del student["name"]        # Deletes key
student.clear()            # Empties dictionary

# checking keys & values
student = {"name": "Ravi", "age": 25}
print("name" in student)   # True
print(25 in student.values())  # True

# looping through dictionaries
student = {"name": "Ravi", "age": 25}
for key in student:
    print(key, student[key])

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key} → {value}")

# Nested dictionaries
students = {
    "101": {"name": "Ravi", "age": 25},
    "102": {"name": "Priya", "age": 23}
}
print(students["101"]["name"])  # Ravi

# dictionary comprehesions
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# built-in methods
student = {"name": "Ravi", "age": 25}
print(student.keys())      # dict_keys(['name', 'age'])
print(student.values())    # dict_values(['Ravi', 25])
print(student.items())     # dict_items([('name', 'Ravi'), ('age', 25)])

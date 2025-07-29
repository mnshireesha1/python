age = 18

if age >= 18:
    print("You are eligible to vote.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")


#Logical Operators
x = 10
if x > 5 and x < 15:
    print("x is between 5 and 15")

if x < 5 or x > 15:
    print("x is outside the range")

if not x == 5:
    print("x is not 5")


#for loop
for i in range(5):
    print(i)

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)


#while loop
i = 1
while i <= 5:
    print(i)
    i += 1


# break: exits the loop
for i in range(10):
    if i == 5:
        break
    print(i)

# continue: skips current loop
for i in range(5):
    if i == 2:
        continue
    print(i)

# pass: does nothing (used as placeholder)
for i in range(3):
    pass  # Code to be written later

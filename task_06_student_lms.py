print("=" * 30)
print("Enhanced LMS Grade Tracker")
print("=" * 30)

# 1. Student ID validation
student_id_valid = False
while not student_id_valid:
    student_id = input("Enter Student ID: ")
    if student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else: 
            print("Enter Non-zero Number")
    else:
        print("Enter valid ID: ID should be Number")

# Format ID like STU00001
formatted_student_id = "STU" + str(student_id).zfill(5)

# 2. Student Name validation and formatting
student_name_valid = False
while not student_name_valid:
    student_name = input("Enter Student Name: ").strip()
    if len(student_name) >= 3 and all(char.isalpha() or char.isspace() for char in student_name):
        # Remove extra spaces and format to Proper Case
        student_name = ' '.join(student_name.split())
        student_name = student_name.title()
        student_name_valid = True
    else:
        print("Name should be at least 3 letters long and contain only letters and spaces")

# Extract first name
first_name = student_name.split()[0].lower()

# Generate email
email = f"{first_name}.{student_id}@university.edu"

# 3. Course Fee Validation
course_fee_valid = False
while not course_fee_valid:
    try:
        course_fee = float(input("Enter Base Course Fee: ₹"))
        if course_fee > 0:
            course_fee_valid = True
        else:
            print("Fee should be positive")
    except ValueError:
        print("Enter a valid number")

# 4. Discount Description Input and Discount Logic
description = input("Enter Description (scholarship, promo, reference): ").lower()

discount = 0
if "scholarship" in description:
    discount = 7000
elif "reference" in description:
    discount = 5000
elif "promo" in description:
    discount = 3000

final_fee = course_fee - discount

# Final Display
print("\n" + "=" * 30)
print("Student Profile Summary")
print("=" * 30)
print(f"Student ID       : {formatted_student_id}")
print(f"Student Name     : {student_name}")
print(f"University Email : {email}")
print(f"Base Fee         : ₹{course_fee}")
print(f"Discount Applied : ₹{discount}")
print(f"Final Fee        : ₹{final_fee}")

student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")
attendance = float(input("Enter Student Attendance: "))
subject_count = 0
total_score = 0

# Calculating Total Score:
while True:
    score = float(input(f"Enter score for subject {subject_count+1}: "))

    total_score += score
    subject_count += 1

    continue_input = input("Do you want to enter another score? (yes/No): ")

    if continue_input.lower() != "yes":
        break
    
# Calculate Average
average_score = total_score / subject_count

# Determine performance
if average_score >= 85:
    performance = "Excellent"
elif average_score >= 70:
    performance = "Good"
elif average_score >= 50:
    performance = "Average"
else:
    performance = "Needs Improvement"

# Attendance Check
if attendance < 75:
    attendance_status = "WARNING: Low Attendance"
else:
    attendance_status = "OK: Attendance Satisfied"

print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Subjects Entered: {subject_count}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")
print(f"Performance Level: {performance}")
print(f"Attendance (%): {attendance}%")
print(f"Attendance Status: {attendance_status}")
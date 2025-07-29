student_name = input("Enter Student name: ")
grade = int(input("Enter Student's grade level (1-12): "))
tuition_fee = int(input("Enter Base Tuition Fee: "))
topper = input("Enter whether the student is an academic topper or not (yes/no): ")

if not (1 <= grade <= 12):
    print("Grade is not valid. Enter between 1 and 12")
else:
    discount = 0

    # Base discount based on grade and topper status
    if 9<=grade<=12:
        if topper.lower()=="yes":
            discount = 20
        else:
            discount = 10
    elif 6<=grade<=8:
        discount = 5
    else:
        discount = 0

    #for additional discounts:
    match grade:
        case 10:
            discount += 3
        case 12:
            discount += 5

discount_amount = (discount / 100) * tuition_fee
final_total_fee = tuition_fee - discount_amount


print(f"Student name: {student_name}")
print(f"Grade Level: {grade}")
print(f"Academic Topper status: {topper}")
print(f"Base Tuition Fee: {tuition_fee}")
print(f"Total discount percentage: {discount}%")
print(f"Discount amount saved: {discount_amount}")
print(f"Final tuition fee after discount: {final_total_fee}")
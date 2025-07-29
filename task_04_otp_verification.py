# Pre-defined correct OTP
correct_otp = "5678"  # You can change it to any 4-digit number
attempts = 3

while attempts > 0:
    user_otp = input("Enter 4-digit OTP: ")

    # Validate OTP length and numeric check
    if not user_otp.isdigit() or len(user_otp) != 4:
        print("OTP must be a 4-digit number only.")
        continue

    # Check if OTP matches
    if user_otp == correct_otp:
        print("Correct OTP - Success!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect OTP. You have {attempts} attempt(s) left.")
        else:
            print("Maximum attempts done, try after 24 Hours.")

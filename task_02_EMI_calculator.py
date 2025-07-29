# Car Loan EMI Calculator

car_name = input("Enter Car Name: ")
car_variant = input("Enter Car Variant: ")
on_road_price = int(input("Enter On-Road price: "))
down_payment = int(input("Enter Down Payment: "))
interest = float(input("Enter Annual Interest Rate (in %): "))
loan_period = int(input("Enter Loan Period in years: "))

# Calculations
total_loan_amount = on_road_price - down_payment
monthly_interest_rate = (interest / 100) / 12  #  Convert to monthly decimal rate
total_loan_duration = loan_period * 12

# EMI Formula: [P x R x (1+R)^N] / [(1+R)^N - 1]
P = total_loan_amount
R = monthly_interest_rate
N = total_loan_duration

emi = (P * R * (1 + R)**N) / ((1 + R)**N - 1)

print(f"EMI Details for {car_name} - {car_variant}")
print(f"Loan Amount: ₹{P}")
print(f"Loan Duration: {N} months")
print(f"Monthly EMI: ₹{emi}")

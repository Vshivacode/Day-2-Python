# Tip Calculator
print("Welcome to Tip Calculator")
bill = int(input("Enter your Bill amount: "))
person = int(input("How many persons are there?: "))
tip = int(input("How much do you want to give the tip? (in percentage): "))    # example: 10%, 12%, 15%
tip_amount = 100 * (tip / 100)
bill_with_tip = bill + tip_amount
total_bill = bill_with_tip / person
print(f"Each person needs to pay Rs:{total_bill}")


# Output:
# Welcome to Tip Calculator
# Enter your Bill amount: 1200
# How many persons are there?: 5
# How much do you want to give the tip? (in percentage): 2
# Each person needs to pay Rs:240.4


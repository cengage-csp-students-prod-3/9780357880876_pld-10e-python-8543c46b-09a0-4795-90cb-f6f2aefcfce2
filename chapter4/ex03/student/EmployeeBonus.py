# EmployeeBonus.py - This program calculates 
# initialize variables here.
bonus_1 = 50.00
bonus_2 = 75.00
bonus_3 = 100.00
bonus_4 = 200.00
bonus = 0
employee_name = input("Enter employee's name: ")
shift_string = input("Enter number of shifts: ")
transact_string = input("Enter number of transactions: ")
dollar_string = input("Enter transactions dollar value: ")

num_shifts = float(shift_string)
num_transactions = float(transact_string)
dollar_value = float(dollar_string)

# Write your code here
score = dollar_value / num_transactions / num_shifts
if score  <= 30:
    bonus = bonus_1
elif score > 30: 
    if score < 70:
        bonus= bonus_2
elif score >= 70 :
    if score < 200:
        bonus = bonus_3
else: 
    bonus= bonus_4
    
# Output.
print("Employee Name:", employee_name)
print(f"Employee Bonus: ${bonus:.2f}")
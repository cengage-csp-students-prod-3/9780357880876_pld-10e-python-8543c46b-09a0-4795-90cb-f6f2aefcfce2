



BONUS_1 = 50
BONUS_2 = 75
BONUS_3 = 100
BONUS_4 = 200



# Get input from the user
employee_name = input("Employee’s name: ")
number_of_shifts = int(input("Number of Shifts: "))
number_of_transactions = int(input("Number of transactions: "))
dollar_value = float(input("Transaction dollar value: "))

# Calculate productivity score
productivity_score = dollar_value / (number_of_transactions * number_of_shifts)

# Determine bonus using nested if statements
if productivity_score <= 30:
    bonus = BONUS_1
else:
    if productivity_score < 70:
        bonus = BONUS_2
    else:
        if productivity_score < 200:
            bonus = BONUS_3
        else:
            bonus = BONUS_4

# Display the results
print("Employee Name: " + employee_name)
print(f"Employee Bonus: ${bonus:.2f}")
# This program calculates an employee's take home pay.
salary = 1250.00
numDependents = 2
stateTax = .065 * salary
federalTax = .28 * salary
dependentDeduction = .025 * salary *numDependent
totalWithholding = stateTax + federalTax
takeHomePay = salary - totalWithholding + dependentDeduction

# Calculate state tax here.

print(f"State Tax: ${stateTax:.2f}")

# Calculate federal tax here.

print(f"Federal Tax: ${federalTax:.2f}")

# Calculate dependant deduction here.

print(f"Dependents: ${dependentDeduction:.2f}")

# Calculate total withholding here.

print(f"Total withholding ${totalWithholding:.2f}")


# Calculate take home pay here.

print(f"Salary: ${salary:.2f}")
print(f"Take-Home Pay: ${takeHomePay:.2f}")
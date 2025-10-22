# LetterE.py - This program prints the letter E with 3 asterisks
# across and 5 asterisks down.
# Input:  None.
# Output: Prints the letter E.

num_across = 3  # Number of asterisks to print across.
num_down = 5  # Number of asterisks to print down.

# Write a loop to control the number of rows.
for row in range(num_down):
# Write a loop to control the number of columns
    for col in range(num_across):
# Decide when to print an asterisk in every column.
       if col == 0 or row == 0 or row ==num_down //2 or row == num_down-1:
           print("*", end=" ")
       else:
           print("", end="")
# Figure out where to place this statement that prints a newline.

print()
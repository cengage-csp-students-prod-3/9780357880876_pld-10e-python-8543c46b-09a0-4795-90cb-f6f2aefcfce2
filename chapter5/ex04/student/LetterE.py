# LetterE.py - This program prints the letter E with 3 asterisks
# across and 5 asterisks down.
# Input:  None.
# Output: Prints the letter E.

num_across = 3  # Number of asterisks to print across.
num_down = 5    # Number of asterisks to print down.

# Write a loop to control the number of rows.
for row in range(num_down):
    # Write a loop to control the number of columns.
    for col in range(num_across):
        # Decide when to print an asterisk or a space based on row and column.
        if col ==  0:
            print("*", end="")
        else:
            # For all other cases, print a space.
            if row ==0 or row == num_down // 2 or row == num_down -1:
                print("*", end="")
            else:
                print(" ", end = " ")

    # Place this statement that prints a newline after the inner loop finishes.
    print()
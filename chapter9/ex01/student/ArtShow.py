# ArtShow.py - This program determines if an art show attendee gets a 5% discount
# for preregistering.
# Input:  Interactive.
# Output:  A statement telling the user if they get a discount or no discount.
def discount():
	print("You are pre-registered and qualify for a 5% discount.")

# Write noDiscount function here.
def nodiscount():
	print("Sorry, you did not pre-register and do not qualify for a 5% discount.")


def main():

		registerString = input("Did you preregister? Enter Y or N: ")
		if	registerString == "y":
			discount()
		else:
			nodiscount()
		# Test input here. If Y, call discount(), else call noDiscount().

# End of main() function.


# Write discount function here.


# Call the main function to run program
main()
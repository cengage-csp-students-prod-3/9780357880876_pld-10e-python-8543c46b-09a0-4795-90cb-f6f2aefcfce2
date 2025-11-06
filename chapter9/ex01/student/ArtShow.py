# ArtShow.py - This program determines if an art show attendee gets a 5% discount
# for preregistering.
# Input:  Interactive.
# Output:  A statement telling the user if they get a discount or no discount.



def discount():
	print("You are pre-registered and qualify for a 5% discount.")

# Write noDiscount function here.
def nodiscount():
	print("Sorry, you did not pre-register and do not qualify for a 5% discount.")


		# Test input here. If Y, call discount(), else call noDiscount().

# End of main() function.
def main():

		registerString = input("Did you preregister? Enter Y or N: ")
		if	registerString == "Y":
			discount()
		else:
			nodiscount()

# Write discount function here.


# Call the main function to run program
if __name__ == "__main__":
    main()
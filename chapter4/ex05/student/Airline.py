passengerName = input("Enter passenger's name: ") # Passenger's name.
ageString = input("Enter passenger's age: ") # string version of passenger's age.

passengerAge = int(ageString) # Passenger's age.

if passengerAge <= 6 or passengerAge >= 65 :   
    print("Passenger is eligible for a discount.")
else:
    print("Passenger is not eligible for a discount.")

# Test to see if this passenger is eligible for a 25% discount.
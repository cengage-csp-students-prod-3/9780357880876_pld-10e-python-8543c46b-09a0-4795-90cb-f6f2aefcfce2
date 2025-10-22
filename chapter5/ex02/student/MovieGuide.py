# MovieGuide.py - This program allows each theater patron to enter a value from 0 to 4
# indicating the number of stars that the patron awards to the Guide's featured movie of the
# week. The program executes continuously until the theater manager enters a negative number to
# quit. At the end of the program, the average star rating for the movie is displayed.

totalStars = 0  # total of star ratings.
numPatrons = 0  # keep track of number of patrons
# Get input.
numStarsInput = int (input("Enter rating for featured movie:"))
# Convert to int.

# Write while loop here
while numStarsInput >= 0 :   
        totalStars += numStarsInput 
        numPatrons += 1
        numStarsInput = int (input("Enter rating for featured movie:"))

totalStars = totalStars / numPatrons
print("Average Star Value:", totalStars)
# Calculate average star rating



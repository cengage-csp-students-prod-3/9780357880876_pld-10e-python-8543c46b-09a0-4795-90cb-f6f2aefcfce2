# Initialize an integer for list size here.

numList = 8

# Initialize list here.
averages = []
averageAll=0

# Write a loop to get batting averages from user and add to list.
for i in range(numList):
    battingAverageString = input(str("Enter a batting average "))
    battingAverageFloat = float(battingAverageString)
    averages.append(battingAverageFloat)




# Use these variables to store the minimim and maximum batting averages.

# Assign the first element in the list to be the minimum and the maximum.

min = averages[0]

max = averages[0]


# Start out your total initialized to 0.

total = 0 

# Write a loop here to access list values starting with averages[1]
for i in averages:
    if i < min:
        min = i
    if i > max:
        max = i
    total += i




    # Within the loop test for minimum and maximum batting averages.

averageAll = total / numList
    # Also accumulate a total of all batting averages.


print("Minimum batting average is " , min)
print("Maximum batting average is " , max)
print("Average batting average is ", averageAll)

# Calculate the average of the 8 averages.



# Print the averages stored in the averages list.



# Print the maximum batting average, minimum batting average, and average batting average.

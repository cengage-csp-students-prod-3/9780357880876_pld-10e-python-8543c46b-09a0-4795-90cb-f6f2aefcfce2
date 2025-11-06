# Computation.py - This program calculates sum, difference, and product of two values.
# Input:  Interactive.
# Output:  Sum, difference, and product of two values.

def main(value1, value2):

    value1String = input("Enter first numeric value: ")
    value1 = float(value1String)
    value2String = input("Enter second numeric value: ")
    value2 = float(value2String)


    # Call calculateSum() here
calculateSum()
    # Call calculateDifference() here
calculateDifference()
    # Call calculateProduct() here
calculateProduct()
# End of main() function.

# Write calculateSum() function here.
def calculateSum(value1, value2):
    result = value1 + value2

# Write calculateDifference() function here.
def calculateDifference(value1,value2):
    resultDiff= value1-value2

# Write calculateProduct() function here.
def calculateProduct(value1, value2):
    resultproduct = value1 * value2

if __name__ == '__main__':
    main()
# Call the main function to run program
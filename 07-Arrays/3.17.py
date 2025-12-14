# Write a program that counts the number of occurrences of any value from a tuple. Sample result:

# Tuple: 50,20,40,50,30,50
# Value: 50
# Number of occurrences: 3


def count(tupl, value):
    print("Tuple:", tupl)
    print("Value:", value)

    occurrence = tupl.count(value)
    print("Number of occurrences:", occurrence)

print(count((50, 20, 40, 50, 30, 50), 50))

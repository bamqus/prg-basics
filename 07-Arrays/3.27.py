# A two-dimensional array of size 2 by 4 contains integer numbers. 
# Create a program that prints array values in rows and columns.


arr = [
    [0,2,1,4],
    [1,2,3,4]
]

for i in arr:
    for x in i:
        print(x, end=" ")
    print("")


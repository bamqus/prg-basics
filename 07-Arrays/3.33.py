# A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last column. 
# Print array values in rows and columns before and after changes.

# Print array values in rows and columns before and after changes.

arr = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]


]


arr[0][0],arr[1][0],arr[2][0] = arr[0][4],arr[1][4],arr[2][4]

for i in arr:
    print(*i)
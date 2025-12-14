# The following array represents a square matrix and contains values:

# [
#    [0,0,0],
#    [0,0,0],
#    [0,0,0]
# ]
# Create a program that replaces the values of the main diagonal with 1.
#  Use a loop statement. Print the modified array. Sample result:

# 1 0 0
# 0 1 0
# 0 0 1

arr = [
     [0,0,0],
     [0,0,0],
     [0,0,0]
]

for i in range(len(arr)):
    arr[i][i] += 1
    for x in arr[i]:
        print(x, end=" ")
    print("")


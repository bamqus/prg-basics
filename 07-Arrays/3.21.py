# Write a program that checks whether the first array is a subset of the second one 
# (whether all elements of the first array appear in the second array).

def check(arr1, arr2):
    return set(arr1).issubset(arr2)

print(check([1,2,2,2,5],[1,2,3,4,5]))

# niewychodzi
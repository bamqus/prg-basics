# Define a function compare(array1, array2) that returns True if
# both arrays are the same or False otherwise. 
# Two arrays  are the same if they have the same number of elements and values of elements in 
# cells of arrays with the same index are equal. 
# Then create a program and try to compare the following arrays:

# 1.["water","book","sky"]   ["water","book","sky"]
# 1. [True,False]   [True,False,True]
# 1. [5,3,1]   [5,3,1]
# 1. [3,2,1]   [3,2]
# Print both arrays and the result of comparison. Sample result:

# Array1: water book sky
# Array2: water book sky
# Comparison: arrays are the same


def compare(array1, array2):
    print(f"Array1:", *array1)
    print(f"Array2:", *array2)



    if len(array1) != len(array2):
        print(f"Comparison: arrays are not the same")
        return False

    
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            print(f"Comparison: arrays are not the same")
            return False
    print(f"Comparison: arrays are the same")
    return True

    

print(compare([3,2,1] ,  [3,2]))

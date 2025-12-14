# Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. 
# Create a program that prints the numbers from the first array that do not appear in the second array.

def numbers(array1,array2):
    result = []
    for i in array1:
        if i not in array2:
            result.append(i)
    return result
 

print(numbers([4,36,12,28,9,44,5] , [5,1,36]))

            

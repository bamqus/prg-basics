# Write a program to separate even and odd numbers of a given array of integers. 
# Put all even numbers first, and then odd numbers.

# Sample result:

# arr = [7,9,2,4,5,6]
# ...
# ...
# arr = [2,4,6,7,9,5]
result = []
result1 = []
def separate(array):
    for i in array:
        if i % 2 == 0:
            result.append(i)
        
        else:
            result1.append(i)
    print(result + result1)


print(separate([7,9,2,4,5,6]))
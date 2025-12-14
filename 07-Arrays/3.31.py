# An array contains integer numbers:

# [[-38, 19], [5,40],[-7,11],[29,16]]
# Create a program that finds the smallest 
# and largest values in the array and in which row and column they are located.

arr = [[-38, 19], [5,40],[-7,11],[29,16]]


smallest = arr[0][0]
largest = arr[0][0]
for i in arr:
    for x in i:
        if x < smallest:
            smallest = x
    
    for x in i:
        if x > largest:
            largest = x
       

print(smallest , largest)

        

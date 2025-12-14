# Define a function occurs(number, array) that returns True if a given number is present in an array. 
# Then create a program that checks whether the number entered from the keyboard is present in the array 
# [15, 38, 7, 23, 14]. Sample result:

# Number: 23
# Array: 15 38 7 23 14
# Result: number 23 appears in the array

def occurs(numbers, array):
     print("Number:",numbers)
     print("Array:",*array)

     if numbers not in array:
          print("Number",numbers,"doesn't appear in the array")
          return False
     else:
          print("Number",numbers,"appears in the array")
          return True
     
print(occurs(22, [15,38,7,23,14] ))


# Write a program that, for the given array of real numbers, 
# prints the number of elements that are greater than the given value entered from the keyboard.

def numbers(number, array):
    result = 0
    for i in array:
        if i > number:
            result += 1
    return result

print(numbers(1,[2,1,0,4]))

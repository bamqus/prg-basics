
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Third value', arr[-1])
print('Second to last value', arr[3])
print('Sum of first and last value', int(arr[0]) + int(arr[-1]))
print('Middle value', arr[len(arr)//2])

print('Array values separated by single space', end=" ")
for i in range(len(arr)):
    print(arr[i], end=" ")
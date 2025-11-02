first = input('Enter first letter: ').upper()
last = input('Enter last letter: ').upper()

first_code = ord(first)
last_code = ord(last)
gap = abs(last_code - first_code) - 1
number_of_letters = max(0, gap)

print(f'Between {first} and {last} is {number_of_letters} letters')
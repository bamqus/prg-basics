import math

r = float(input('Enter radius: '))
pi = math.pi

area = pi * r**2
circumference = 2 * pi * r

print(f'Circumference: {circumference:.2f}')
print(f'Area: {area:.2f}')
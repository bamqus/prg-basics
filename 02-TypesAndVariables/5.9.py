import math

circ = float(input('Enter tree circumference in cm: '))
diameter = circ / math.pi
can_cut = diameter >= 50
print(f'Tree can be cut down: {can_cut}')